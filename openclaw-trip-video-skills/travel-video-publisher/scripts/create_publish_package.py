#!/usr/bin/env python3
"""Create platform publish packages from an approved video package."""

import json
import sys
from pathlib import Path


def main():
    if len(sys.argv) != 3:
        print("Usage: create_publish_package.py <approved_package.json> <publish_jobs.json>", file=sys.stderr)
        return 2
    data = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8-sig"))
    if data.get("qa_decision") not in ("approve", "approved", None):
        print("QA is not approved", file=sys.stderr)
        return 1
    platforms = data.get("platform_targets") or data.get("platforms") or ["manual_queue"]
    jobs = []
    for platform in platforms:
        jobs.append({
            "platform": platform,
            "video_url": data.get("video_url") or data.get("final_video_url"),
            "cover_url": data.get("cover_url"),
            "title": data.get("title"),
            "caption": data.get("caption"),
            "hashtags": data.get("hashtags", []),
            "status": "manual_required"
        })
    Path(sys.argv[2]).write_text(json.dumps({"platform_jobs": jobs}, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote {len(jobs)} publish jobs")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
