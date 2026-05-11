#!/usr/bin/env python3
"""Validate a travel video render manifest."""

import json
import sys
from pathlib import Path


def main():
    if len(sys.argv) != 2:
        print("Usage: validate_render_manifest.py <render_manifest.json>", file=sys.stderr)
        return 2
    data = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8-sig"))
    manifest = data.get("render_manifest", data)
    errors = []
    export = manifest.get("export", {})
    for key in ("width", "height", "fps", "duration_seconds"):
        if not export.get(key):
            errors.append(f"missing export.{key}")
    last_end = 0
    for scene in manifest.get("timeline", []):
        start = scene.get("start_sec")
        end = scene.get("end_sec")
        if start is None or end is None or end <= start:
            errors.append(f"invalid timing for {scene.get('scene_id')}")
        if start is not None and abs(float(start) - float(last_end)) > 0.05:
            errors.append(f"timeline gap before {scene.get('scene_id')}")
        if end is not None:
            last_end = end
    print(json.dumps({"valid": not errors, "errors": errors}, indent=2))
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
