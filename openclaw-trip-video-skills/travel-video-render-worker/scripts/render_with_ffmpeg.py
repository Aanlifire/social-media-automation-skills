#!/usr/bin/env python3
"""Render a vertical MP4 from a travel-video render manifest using FFmpeg.

This is a deterministic fallback renderer. It supports video/image/SVG layers as
full-frame scene backgrounds, plus a single voiceover track when provided.
Complex multi-layer templates should be delegated to a Remotion/video-worker.
"""

import argparse
import json
import os
import shutil
import subprocess
import tempfile
from pathlib import Path


def ffmpeg_path():
    return os.getenv("FFMPEG_PATH") or shutil.which("ffmpeg")


def ffprobe_path():
    return os.getenv("FFPROBE_PATH") or shutil.which("ffprobe")


def source_for_layer(layer, assets):
    asset_id = layer.get("asset_id")
    item = assets.get(asset_id, {})
    return item.get("local_path") or item.get("uri") or item.get("source")


def build_asset_map(data):
    assets = {}
    for section in ("media_results", "stored_assets"):
        for item in data.get(section, []):
            key = item.get("request_id") or item.get("asset_id")
            if key:
                assets[key] = item
    for item in data.get("assets", []):
        key = item.get("asset_id") or item.get("request_id")
        if key:
            assets[key] = item
    return assets


def render_scene(ffmpeg, source, width, height, fps, duration, target):
    if not source:
        raise RuntimeError("scene has no source asset")
    source_path = str(source)
    image_ext = Path(source_path).suffix.lower()
    if image_ext in {".png", ".jpg", ".jpeg", ".webp", ".svg"}:
        cmd = [
            ffmpeg, "-y", "-loop", "1", "-t", str(duration), "-i", source_path,
            "-vf", f"scale={width}:{height}:force_original_aspect_ratio=increase,crop={width}:{height},fps={fps},format=yuv420p",
            "-an", str(target),
        ]
    else:
        cmd = [
            ffmpeg, "-y", "-t", str(duration), "-i", source_path,
            "-vf", f"scale={width}:{height}:force_original_aspect_ratio=increase,crop={width}:{height},fps={fps},format=yuv420p",
            "-an", str(target),
        ]
    completed = subprocess.run(cmd, text=True, capture_output=True)
    if completed.returncode != 0:
        raise RuntimeError(completed.stderr[-2000:])


def concat_scenes(ffmpeg, scenes, target):
    list_file = target.parent / "concat.txt"
    list_file.write_text("".join(f"file '{str(scene).replace('\\', '/')}'\n" for scene in scenes), encoding="utf-8")
    completed = subprocess.run([ffmpeg, "-y", "-f", "concat", "-safe", "0", "-i", str(list_file), "-c", "copy", str(target)], text=True, capture_output=True)
    if completed.returncode != 0:
        raise RuntimeError(completed.stderr[-2000:])


def mux_audio(ffmpeg, video, audio, target):
    cmd = [ffmpeg, "-y", "-i", str(video), "-i", str(audio), "-map", "0:v:0", "-map", "1:a:0", "-c:v", "copy", "-c:a", "aac", "-shortest", str(target)]
    completed = subprocess.run(cmd, text=True, capture_output=True)
    if completed.returncode != 0:
        raise RuntimeError(completed.stderr[-2000:])


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("render_package")
    parser.add_argument("output_json")
    parser.add_argument("--output-dir", default="rendered")
    args = parser.parse_args()

    ffmpeg = ffmpeg_path()
    if not ffmpeg:
        Path(args.output_json).write_text(json.dumps({
            "status": "blocked",
            "render_mode": "blocked",
            "missing_configuration": ["FFMPEG_PATH or ffmpeg in PATH"],
            "errors": [],
            "next_node": "human_setup_required",
        }, ensure_ascii=False, indent=2), encoding="utf-8")
        return 0

    data = json.loads(Path(args.render_package).read_text(encoding="utf-8-sig"))
    manifest = data.get("render_manifest", data)
    assets = build_asset_map(data)
    export = manifest.get("export", {})
    width = int(export.get("width", 1080))
    height = int(export.get("height", 1920))
    fps = int(export.get("fps", 30))
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    final_path = output_dir / "video.mp4"
    cover_path = output_dir / "cover.jpg"
    logs = []
    try:
        with tempfile.TemporaryDirectory() as td:
            temp = Path(td)
            scene_files = []
            for index, scene in enumerate(manifest.get("timeline", []), start=1):
                layers = scene.get("layers", [])
                source = None
                for layer in layers:
                    if layer.get("type") in {"video", "image", "ui_card", "map_animation", "overlay"}:
                        source = source_for_layer(layer, assets)
                        if source:
                            break
                duration = float(scene.get("end_sec", 0)) - float(scene.get("start_sec", 0))
                scene_target = temp / f"scene-{index:03d}.mp4"
                render_scene(ffmpeg, source, width, height, fps, max(duration, 0.1), scene_target)
                scene_files.append(scene_target)
            silent_video = temp / "silent.mp4"
            concat_scenes(ffmpeg, scene_files, silent_video)
            audio_source = None
            for track in manifest.get("audio_tracks", []):
                audio_source = source_for_layer({"asset_id": track.get("asset_id")}, assets)
                if audio_source:
                    break
            if audio_source:
                mux_audio(ffmpeg, silent_video, audio_source, final_path)
            else:
                shutil.copyfile(silent_video, final_path)
            subprocess.run([ffmpeg, "-y", "-ss", str(manifest.get("cover_export", {}).get("frame_sec", 1)), "-i", str(final_path), "-frames:v", "1", str(cover_path)], text=True, capture_output=True)
    except Exception as exc:
        Path(args.output_json).write_text(json.dumps({
            "status": "failed",
            "render_mode": "ffmpeg",
            "final_video": {},
            "cover": {},
            "logs": logs,
            "missing_configuration": [],
            "errors": [str(exc)],
            "next_node": "editing_plan",
        }, ensure_ascii=False, indent=2), encoding="utf-8")
        return 1

    Path(args.output_json).write_text(json.dumps({
        "status": "rendered",
        "render_mode": "ffmpeg",
        "render_job_id": final_path.stem,
        "final_video": {
            "local_path": str(final_path),
            "uri": "",
            "width": width,
            "height": height,
            "fps": fps,
        },
        "cover": {"local_path": str(cover_path), "uri": ""},
        "logs": logs,
        "missing_configuration": [],
        "errors": [],
        "next_node": "oss_storage",
    }, ensure_ascii=False, indent=2), encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
