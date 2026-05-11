#!/usr/bin/env python3
"""Submit approved publish jobs to a configured HTTP publisher endpoint.

The endpoint is expected to accept POST JSON and return a job response. If no
endpoint is configured, the script leaves jobs in manual_required state.
"""

import argparse
import json
import os
import urllib.error
import urllib.request
from pathlib import Path


def post_json(url, payload, token=None):
    body = json.dumps(payload).encode("utf-8")
    headers = {"Content-Type": "application/json"}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    request = urllib.request.Request(url, data=body, headers=headers, method="POST")
    with urllib.request.urlopen(request, timeout=120) as response:
        return json.loads(response.read().decode("utf-8"))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("publish_jobs")
    parser.add_argument("output_json")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    data = json.loads(Path(args.publish_jobs).read_text(encoding="utf-8-sig"))
    jobs = data.get("platform_jobs", [])
    endpoint = os.getenv("PUBLISHER_ENDPOINT", "")
    token = os.getenv("PUBLISHER_TOKEN", "")
    results = []
    missing = [] if endpoint or args.dry_run else ["PUBLISHER_ENDPOINT"]
    for job in jobs:
        result = dict(job)
        if args.dry_run or not endpoint:
            result.setdefault("status", "manual_required")
            result["publish_mode"] = "manual_queue"
        else:
            try:
                response = post_json(endpoint, job, token)
                result["status"] = response.get("status", "submitted")
                result["publish_job_id"] = response.get("publish_job_id") or response.get("id", "")
                result["publish_mode"] = "official_api"
            except (urllib.error.URLError, TimeoutError, ValueError) as exc:
                result["status"] = "failed"
                result["publish_mode"] = "official_api"
                result["risk_notes"] = result.get("risk_notes", []) + [str(exc)]
        results.append(result)
    status = "blocked" if missing else ("ok" if all(job.get("status") in {"submitted", "draft_created", "manual_required"} for job in results) else "failed")
    Path(args.output_json).write_text(json.dumps({
        "status": status,
        "publish_mode": "manual_queue" if missing or args.dry_run else "official_api",
        "platform_jobs": results,
        "missing_configuration": missing,
        "next_node": "human_review" if missing or args.dry_run else "published",
    }, ensure_ascii=False, indent=2), encoding="utf-8")
    return 0 if status != "failed" else 1


if __name__ == "__main__":
    raise SystemExit(main())
