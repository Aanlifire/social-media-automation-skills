# Output Schema

Return JSON only.

```json
{
  "status": "ok | blocked | partial | failed",
  "missing_configuration": ["string"],
  "media_results": [
    {
      "request_id": "asset-001",
      "type": "image | video | tts | cover | ui_card | overlay | map_animation",
      "provider": "string",
      "provider_task_id": "string",
      "status": "submitted | processing | ready | failed | pending_provider",
      "uri": "string",
      "local_path": "string",
      "duration_seconds": 0,
      "width": 1080,
      "height": 1920,
      "retryable": false,
      "error": "string"
    }
  ],
  "next_node": "oss_storage | editing_plan | asset_generation | human_setup_required"
}
```
