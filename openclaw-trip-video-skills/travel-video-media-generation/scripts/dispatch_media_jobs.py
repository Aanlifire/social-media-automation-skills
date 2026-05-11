#!/usr/bin/env python3
"""Build dispatchable media jobs from an asset plan JSON.

This script does not call a vendor directly. It validates the contract and
creates stable job records for a configured media worker or provider adapter.
"""

import json
import sys
from pathlib import Path


def main():
    if len(sys.argv) != 3:
        print("Usage: dispatch_media_jobs.py <asset_plan.json> <jobs.json>", file=sys.stderr)
        return 2
    source = Path(sys.argv[1])
    target = Path(sys.argv[2])
    data = json.loads(source.read_text(encoding="utf-8-sig"))
    plan = data.get("asset_plan", data)
    jobs = []
    for scene in plan.get("scene_assets", []):
        for req in scene.get("requests", []):
            jobs.append({
                "job_id": req.get("request_id"),
                "scene_id": scene.get("scene_id"),
                "type": req.get("type"),
                "prompt": req.get("prompt"),
                "duration_seconds": req.get("duration_seconds"),
                "aspect_ratio": req.get("aspect_ratio", plan.get("aspect_ratio", "9:16")),
                "status": "pending_provider"
            })
    for req in plan.get("shared_assets", []):
        jobs.append({
            "job_id": req.get("request_id"),
            "scene_id": "shared",
            "type": req.get("type"),
            "prompt": req.get("prompt"),
            "status": "pending_provider"
        })
    target.write_text(json.dumps({"media_jobs": jobs}, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote {len(jobs)} media jobs to {target}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
