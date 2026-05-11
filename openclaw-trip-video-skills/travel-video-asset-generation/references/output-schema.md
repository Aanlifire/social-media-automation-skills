# Output Schema

Return JSON only.

```json
{
  "status": "ok",
  "assumptions": ["string"],
  "needs_fact_check": false,
  "asset_plan": {
    "platform": "douyin",
    "duration_seconds": 30,
    "aspect_ratio": "9:16",
    "scene_assets": [
      {
        "scene_id": "scene-01",
        "purpose": "hook",
        "primary_asset_type": "video",
        "requests": [
          {
            "request_id": "asset-001",
            "type": "video | image | tts | map_animation | ui_card | overlay | cover",
            "purpose": "string",
            "prompt": "string",
            "duration_seconds": 3,
            "aspect_ratio": "9:16",
            "reusable": false,
            "notes": ["string"]
          }
        ]
      }
    ],
    "shared_assets": [
      {
        "request_id": "shared-001",
        "type": "ui_card | overlay | cover | map_animation",
        "purpose": "string",
        "prompt": "string",
        "reusable": true,
        "notes": ["string"]
      }
    ],
    "downstream_hints": [
      "video_generation",
      "image_generation",
      "tts_generation",
      "graphics_generation",
      "editing"
    ]
  }
}
```

## Request Rules

- Keep request IDs stable and unique.
- Keep scene assets grouped by scene.
- Use `shared_assets` for reusable branded or repeated components.
- Mark requests reusable when the same asset can serve multiple videos or destinations with light edits.
