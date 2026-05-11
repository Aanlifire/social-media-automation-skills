# Output Schema

Return JSON only.

```json
{
  "status": "rendered | submitted | blocked | failed",
  "render_mode": "remotion | ffmpeg | remote_worker | blocked",
  "render_job_id": "string",
  "final_video": {
    "local_path": "string",
    "uri": "string",
    "duration_seconds": 30,
    "width": 1080,
    "height": 1920,
    "fps": 30
  },
  "cover": {
    "local_path": "string",
    "uri": "string"
  },
  "logs": ["string"],
  "missing_configuration": ["string"],
  "errors": ["string"],
  "next_node": "oss_storage | qa_review | editing_plan | human_setup_required"
}
```
