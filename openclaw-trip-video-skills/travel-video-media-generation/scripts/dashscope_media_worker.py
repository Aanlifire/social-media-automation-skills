#!/usr/bin/env python3
"""Generate media assets through DashScope/Wan/Qwen HTTP APIs.

Inputs are media job records from dispatch_media_jobs.py. The script supports:
- video: Wan text-to-video async task
- image/cover: Wan image generation sync call
- tts: Qwen TTS sync call
- ui_card/overlay/map_animation: deterministic SVG placeholders for renderer input

Required for DashScope calls:
- DASHSCOPE_API_KEY

Optional:
- DASHSCOPE_REGION=beijing|singapore|virginia
- DASHSCOPE_BASE_URL=https://dashscope.aliyuncs.com/api/v1
- DASHSCOPE_VIDEO_MODEL=wan2.6-t2v
- DASHSCOPE_IMAGE_MODEL=wan2.6-image
- DASHSCOPE_TTS_MODEL=qwen3-tts-flash
"""

import argparse
import html
import json
import os
import time
import urllib.error
import urllib.request
from pathlib import Path
from urllib.parse import urlparse


REGION_BASE_URLS = {
    "beijing": "https://dashscope.aliyuncs.com/api/v1",
    "singapore": "https://dashscope-intl.aliyuncs.com/api/v1",
    "virginia": "https://dashscope-us.aliyuncs.com/api/v1",
}


def read_json(path):
    return json.loads(Path(path).read_text(encoding="utf-8-sig"))


def write_json(path, data):
    Path(path).write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")


def base_url():
    if os.getenv("DASHSCOPE_BASE_URL"):
        return os.getenv("DASHSCOPE_BASE_URL").rstrip("/")
    return REGION_BASE_URLS.get(os.getenv("DASHSCOPE_REGION", "beijing").lower(), REGION_BASE_URLS["beijing"])


def dashscope_request(method, url, payload=None, extra_headers=None, timeout=120):
    api_key = os.getenv("DASHSCOPE_API_KEY")
    if not api_key:
        raise RuntimeError("Missing DASHSCOPE_API_KEY")
    body = None if payload is None else json.dumps(payload).encode("utf-8")
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }
    if extra_headers:
        headers.update(extra_headers)
    request = urllib.request.Request(url, data=body, headers=headers, method=method)
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            return json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"HTTP {exc.code}: {detail}") from exc


def download(url, output_dir, request_id, default_ext):
    parsed = urlparse(url)
    ext = Path(parsed.path).suffix or default_ext
    target = Path(output_dir) / f"{request_id}{ext}"
    with urllib.request.urlopen(url, timeout=300) as response:
        target.write_bytes(response.read())
    return str(target)


def svg_asset(job, output_dir):
    request_id = job.get("job_id") or job.get("request_id")
    title = html.escape((job.get("prompt") or job.get("purpose") or request_id or "asset")[:120])
    kind = html.escape(job.get("type", "asset"))
    target = Path(output_dir) / f"{request_id}.svg"
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="1080" height="1920" viewBox="0 0 1080 1920">
  <rect width="1080" height="1920" fill="#101820"/>
  <rect x="80" y="260" width="920" height="980" rx="28" fill="#f8f5ef"/>
  <text x="120" y="380" font-family="Arial, sans-serif" font-size="42" fill="#1b1b1b">{kind}</text>
  <foreignObject x="120" y="460" width="840" height="650">
    <div xmlns="http://www.w3.org/1999/xhtml" style="font-family:Arial,sans-serif;font-size:56px;line-height:1.25;color:#1b1b1b;font-weight:700;">{title}</div>
  </foreignObject>
  <text x="120" y="1680" font-family="Arial, sans-serif" font-size="34" fill="#f8f5ef">AI travel video asset</text>
</svg>
"""
    target.write_text(svg, encoding="utf-8")
    return str(target)


def submit_video(job, output_dir, poll, download_files):
    url = f"{base_url()}/services/aigc/video-generation/video-synthesis"
    request_id = job.get("job_id") or job.get("request_id")
    duration = int(job.get("duration_seconds") or 5)
    size = job.get("size") or ("720*1280" if job.get("aspect_ratio", "9:16") == "9:16" else "1280*720")
    payload = {
        "model": job.get("model") or os.getenv("DASHSCOPE_VIDEO_MODEL", "wan2.6-t2v"),
        "input": {"prompt": job.get("prompt", "")},
        "parameters": {
            "size": size,
            "duration": max(2, min(duration, 15)),
            "prompt_extend": bool(job.get("prompt_extend", True)),
            "watermark": bool(job.get("watermark", False)),
        },
    }
    if job.get("negative_prompt"):
        payload["input"]["negative_prompt"] = job["negative_prompt"]
    if job.get("audio_url"):
        payload["input"]["audio_url"] = job["audio_url"]
    created = dashscope_request("POST", url, payload, {"X-DashScope-Async": "enable"})
    output = created.get("output", {})
    task_id = output.get("task_id")
    result = {
        "request_id": request_id,
        "type": "video",
        "provider": "dashscope",
        "provider_task_id": task_id,
        "status": "submitted",
        "uri": "",
        "local_path": "",
        "retryable": False,
        "error": "",
    }
    if not poll or not task_id:
        return result
    task_url = f"{base_url()}/tasks/{task_id}"
    deadline = time.time() + int(os.getenv("DASHSCOPE_POLL_TIMEOUT_SECONDS", "900"))
    interval = int(os.getenv("DASHSCOPE_POLL_INTERVAL_SECONDS", "15"))
    while time.time() < deadline:
        queried = dashscope_request("GET", task_url)
        task = queried.get("output", {})
        status = task.get("task_status", "UNKNOWN")
        if status == "SUCCEEDED":
            video_url = task.get("video_url", "")
            result.update({"status": "ready", "uri": video_url})
            if video_url and download_files:
                result["local_path"] = download(video_url, output_dir, request_id, ".mp4")
            return result
        if status in {"FAILED", "CANCELED", "UNKNOWN"}:
            result.update({"status": "failed", "error": json.dumps(task, ensure_ascii=False), "retryable": status != "CANCELED"})
            return result
        time.sleep(interval)
    result.update({"status": "processing", "retryable": True, "error": "poll timeout"})
    return result


def generate_image(job, output_dir, download_files):
    url = f"{base_url()}/services/aigc/multimodal-generation/generation"
    request_id = job.get("job_id") or job.get("request_id")
    size = job.get("size") or ("720*1280" if job.get("aspect_ratio", "9:16") == "9:16" else "1280*720")
    payload = {
        "model": job.get("model") or os.getenv("DASHSCOPE_IMAGE_MODEL", "wan2.6-image"),
        "input": {
            "messages": [{
                "role": "user",
                "content": [{"text": job.get("prompt", "")}],
            }]
        },
        "parameters": {
            "enable_interleave": True,
            "max_images": int(job.get("n") or 1),
            "size": size,
            "watermark": bool(job.get("watermark", False)),
        },
    }
    response = dashscope_request("POST", url, payload)
    image_url = ""
    for choice in response.get("output", {}).get("choices", []):
        for content in choice.get("message", {}).get("content", []):
            if content.get("type") == "image" and content.get("image"):
                image_url = content["image"]
                break
    result = {
        "request_id": request_id,
        "type": job.get("type", "image"),
        "provider": "dashscope",
        "provider_task_id": response.get("request_id", ""),
        "status": "ready" if image_url else "failed",
        "uri": image_url,
        "local_path": "",
        "retryable": False,
        "error": "" if image_url else json.dumps(response, ensure_ascii=False),
    }
    if image_url and download_files:
        result["local_path"] = download(image_url, output_dir, request_id, ".png")
    return result


def generate_tts(job, output_dir, download_files):
    url = f"{base_url()}/services/aigc/multimodal-generation/generation"
    request_id = job.get("job_id") or job.get("request_id")
    payload = {
        "model": job.get("model") or os.getenv("DASHSCOPE_TTS_MODEL", "qwen3-tts-flash"),
        "input": {
            "text": job.get("text") or job.get("prompt") or "",
            "voice": job.get("voice") or os.getenv("DASHSCOPE_TTS_VOICE", "Cherry"),
            "language_type": job.get("language_type") or os.getenv("DASHSCOPE_TTS_LANGUAGE", "Chinese"),
        },
    }
    response = dashscope_request("POST", url, payload)
    audio = response.get("output", {}).get("audio", {}) or {}
    audio_url = audio.get("url", "")
    result = {
        "request_id": request_id,
        "type": "tts",
        "provider": "dashscope",
        "provider_task_id": audio.get("id", response.get("request_id", "")),
        "status": "ready" if audio_url else "failed",
        "uri": audio_url,
        "local_path": "",
        "retryable": False,
        "error": "" if audio_url else json.dumps(response, ensure_ascii=False),
    }
    if audio_url and download_files:
        result["local_path"] = download(audio_url, output_dir, request_id, ".wav")
    return result


def normalize_jobs(data):
    if "media_jobs" in data:
        return data["media_jobs"]
    if "asset_plan" in data:
        jobs = []
        for scene in data["asset_plan"].get("scene_assets", []):
            for req in scene.get("requests", []):
                req = dict(req)
                req["job_id"] = req.get("request_id")
                req["scene_id"] = scene.get("scene_id")
                jobs.append(req)
        jobs.extend(data["asset_plan"].get("shared_assets", []))
        return jobs
    return data if isinstance(data, list) else []


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("jobs_json")
    parser.add_argument("output_json")
    parser.add_argument("--output-dir", default="generated-media")
    parser.add_argument("--poll", action="store_true")
    parser.add_argument("--download", action="store_true")
    args = parser.parse_args()

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    jobs = normalize_jobs(read_json(args.jobs_json))
    results = []
    missing_config = []
    for job in jobs:
        kind = job.get("type")
        try:
            if kind == "video":
                results.append(submit_video(job, output_dir, args.poll, args.download))
            elif kind in {"image", "cover"}:
                results.append(generate_image(job, output_dir, args.download))
            elif kind == "tts":
                results.append(generate_tts(job, output_dir, args.download))
            elif kind in {"ui_card", "overlay", "map_animation"}:
                local_path = svg_asset(job, output_dir)
                results.append({
                    "request_id": job.get("job_id") or job.get("request_id"),
                    "type": kind,
                    "provider": "local-svg",
                    "provider_task_id": "",
                    "status": "ready",
                    "uri": "",
                    "local_path": local_path,
                    "retryable": False,
                    "error": "",
                })
            else:
                results.append({
                    "request_id": job.get("job_id") or job.get("request_id"),
                    "type": kind,
                    "provider": "",
                    "provider_task_id": "",
                    "status": "failed",
                    "uri": "",
                    "local_path": "",
                    "retryable": False,
                    "error": f"Unsupported media type: {kind}",
                })
        except RuntimeError as exc:
            if "DASHSCOPE_API_KEY" in str(exc) and "DASHSCOPE_API_KEY" not in missing_config:
                missing_config.append("DASHSCOPE_API_KEY")
            results.append({
                "request_id": job.get("job_id") or job.get("request_id"),
                "type": kind,
                "provider": "dashscope",
                "provider_task_id": "",
                "status": "pending_provider" if missing_config else "failed",
                "uri": "",
                "local_path": "",
                "retryable": False,
                "error": str(exc),
            })

    statuses = {item["status"] for item in results}
    status = "ok" if statuses <= {"ready", "submitted"} and not missing_config else "partial"
    if missing_config:
        status = "blocked"
    elif all(item["status"] == "failed" for item in results):
        status = "failed"
    write_json(args.output_json, {
        "status": status,
        "missing_configuration": missing_config,
        "media_results": results,
        "next_node": "oss_storage" if status in {"ok", "partial"} else "human_setup_required",
    })
    return 0 if status != "failed" else 1


if __name__ == "__main__":
    raise SystemExit(main())
