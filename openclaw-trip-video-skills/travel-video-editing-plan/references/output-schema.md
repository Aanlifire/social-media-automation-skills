# Output Schema

Return JSON only.

```json
{
  "status": "ok",
  "render_ready": false,
  "render_manifest": {
    "template": "pitfall | budget_compare | route_optimization | ai_plans_my_trip | comment_to_plan",
    "platform": "douyin | xiaohongshu | wechat_channels | tiktok | broad",
    "export": {
      "aspect_ratio": "9:16",
      "width": 1080,
      "height": 1920,
      "fps": 30,
      "duration_seconds": 30
    },
    "timeline": [
      {
        "scene_id": "scene-01",
        "start_sec": 0,
        "end_sec": 3,
        "layers": [
          {
            "layer_id": "layer-001",
            "type": "video | image | subtitle | overlay | ui_card | map_animation | watermark",
            "asset_id": "asset-001",
            "position": "full_frame | top | center | lower_third | endcard",
            "notes": ["string"]
          }
        ]
      }
    ],
    "audio_tracks": [
      {
        "asset_id": "tts-001",
        "start_sec": 0,
        "end_sec": 3,
        "mix": "voiceover"
      }
    ],
    "subtitle_tracks": [
      {
        "scene_id": "scene-01",
        "text": "string",
        "start_sec": 0,
        "end_sec": 3
      }
    ],
    "cover_export": {
      "frame_sec": 1,
      "text": "string"
    }
  },
  "missing_assets": [
    {
      "asset_id": "asset-001",
      "reason": "missing_uri | duration_mismatch | unsupported_format",
      "repair_node": "asset_generation | tts_generation"
    }
  ],
  "next_node": "render_worker | asset_generation | tts_generation | qa_review"
}
```
