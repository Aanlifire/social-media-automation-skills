#!/usr/bin/env python3
"""Upload files to Alibaba Cloud OSS through ossutil.

This script uses an existing ossutil/ossutil64 binary and credentials from the
runtime environment or ossutil config. It intentionally does not handle secrets.

Required:
- OSSUTIL_PATH or `ossutil` / `ossutil64` in PATH
- OSS_BUCKET

Optional:
- OSS_PUBLIC_BASE_URL
"""

import argparse
import json
import os
import shutil
import subprocess
from pathlib import Path


def read_json(path):
    return json.loads(Path(path).read_text(encoding="utf-8-sig"))


def find_ossutil():
    candidates = [
        os.getenv("OSSUTIL_PATH"),
        shutil.which("ossutil64"),
        shutil.which("ossutil"),
    ]
    for candidate in candidates:
        if candidate:
            return candidate
    return None


def public_url(bucket, object_key):
    base = os.getenv("OSS_PUBLIC_BASE_URL", "").rstrip("/")
    if base:
        return f"{base}/{object_key}"
    endpoint = os.getenv("OSS_ENDPOINT", "").replace("https://", "").replace("http://", "").strip("/")
    if endpoint:
        return f"https://{bucket}.{endpoint}/{object_key}"
    return ""


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("upload_manifest")
    parser.add_argument("output_json")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--next-node", choices=["editing_plan", "qa_review", "publisher"])
    args = parser.parse_args()

    manifest = read_json(args.upload_manifest)
    records = manifest.get("uploads", manifest.get("stored_assets", []))
    desired_next_node = args.next_node or manifest.get("next_node") or "editing_plan"
    bucket = os.getenv("OSS_BUCKET")
    ossutil = find_ossutil()
    missing = []
    if not bucket and not args.dry_run:
        missing.append("OSS_BUCKET")
    if not ossutil and not args.dry_run:
        missing.append("OSSUTIL_PATH or ossutil in PATH")
    stored = []
    for item in records:
        source = item.get("source")
        object_key = item.get("object_key")
        result = dict(item)
        result.update({
            "bucket": bucket or "",
            "public_url": public_url(bucket or "", object_key or ""),
            "status": "pending_upload" if missing or args.dry_run else "uploaded",
            "error": "",
        })
        if not source or not object_key:
            result.update({"status": "failed", "error": "missing source or object_key"})
        elif not (str(source).startswith("http://") or str(source).startswith("https://")) and not Path(source).exists():
            result.update({"status": "failed", "error": f"source file not found: {source}"})
        elif not missing and not args.dry_run:
            destination = f"oss://{bucket}/{object_key}"
            completed = subprocess.run([ossutil, "cp", str(source), destination, "-f"], text=True, capture_output=True)
            if completed.returncode != 0:
                result.update({
                    "status": "failed",
                    "error": (completed.stderr or completed.stdout).strip(),
                })
        stored.append(result)

    status = "blocked" if missing else ("ok" if all(x["status"] in {"uploaded", "pending_upload"} for x in stored) else "partial")
    Path(args.output_json).write_text(json.dumps({
        "status": status,
        "missing_configuration": missing,
        "stored_assets": stored,
        "next_node": desired_next_node if status in {"ok", "partial"} else "human_setup_required",
    }, ensure_ascii=False, indent=2), encoding="utf-8")
    return 0 if status != "failed" else 1


if __name__ == "__main__":
    raise SystemExit(main())
