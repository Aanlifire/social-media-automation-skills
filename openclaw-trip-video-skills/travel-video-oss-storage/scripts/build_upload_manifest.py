#!/usr/bin/env python3
"""Create an OSS upload manifest from media or render result JSON."""

import argparse
import json
import mimetypes
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse


def read_json(path):
    return json.loads(Path(path).read_text(encoding="utf-8-sig"))


def extension_for(source, default_ext="bin"):
    parsed = urlparse(str(source))
    source_path = parsed.path if parsed.scheme in {"http", "https"} else str(source)
    suffix = Path(source_path).suffix.lstrip(".")
    return suffix or default_ext


def add_upload(uploads, *, date, video_id, asset_id, asset_type, source, object_key=None):
    if not object_key:
        ext = extension_for(source)
        object_key = f"trip-video/{date:%Y/%m/%d}/{video_id}/{asset_type}/{asset_id}.{ext}"
    uploads.append({
        "asset_id": asset_id,
        "type": asset_type,
        "source": source,
        "object_key": object_key,
        "mime_type": mimetypes.guess_type(str(source))[0] or "application/octet-stream",
        "status": "pending_upload"
    })


def add_media_results(uploads, data, date, video_id):
    for item in data.get("media_results", []):
        source = item.get("local_path") or item.get("uri")
        if not source:
            continue
        add_upload(
            uploads,
            date=date,
            video_id=video_id,
            asset_id=item.get("request_id") or item.get("asset_id"),
            asset_type=item.get("type", "asset"),
            source=source,
        )


def add_render_outputs(uploads, data, date, video_id):
    final_video = data.get("final_video") or {}
    video_source = final_video.get("local_path") or final_video.get("uri")
    if video_source:
        add_upload(
            uploads,
            date=date,
            video_id=video_id,
            asset_id="final-video",
            asset_type="final_video",
            source=video_source,
            object_key=f"trip-video/{date:%Y/%m/%d}/{video_id}/final/video.{extension_for(video_source, 'mp4')}",
        )
    cover = data.get("cover") or {}
    cover_source = cover.get("local_path") or cover.get("uri")
    if cover_source:
        add_upload(
            uploads,
            date=date,
            video_id=video_id,
            asset_id="final-cover",
            asset_type="cover",
            source=cover_source,
            object_key=f"trip-video/{date:%Y/%m/%d}/{video_id}/final/cover.{extension_for(cover_source, 'jpg')}",
        )


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("source_json")
    parser.add_argument("video_id")
    parser.add_argument("manifest_json")
    parser.add_argument("--next-node", choices=["editing_plan", "qa_review", "publisher"])
    args = parser.parse_args()

    date = datetime.now(timezone.utc)
    data = read_json(args.source_json)
    uploads = []
    add_media_results(uploads, data, date, args.video_id)
    add_render_outputs(uploads, data, date, args.video_id)
    next_node = args.next_node or ("qa_review" if data.get("final_video") or data.get("cover") else "editing_plan")
    Path(args.manifest_json).write_text(json.dumps({
        "uploads": uploads,
        "next_node": next_node,
    }, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote {len(uploads)} upload records to {args.manifest_json}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
