# Output Schema

Return JSON only.

```json
{
  "status": "ok | blocked | failed",
  "publish_mode": "official_api | draft_queue | manual_queue | blocked_setup",
  "platform_jobs": [
    {
      "platform": "douyin | xiaohongshu | wechat_channels | tiktok | other",
      "account_id": "string",
      "video_url": "string",
      "cover_url": "string",
      "title": "string",
      "caption": "string",
      "hashtags": ["string"],
      "scheduled_at": "YYYY-MM-DDTHH:mm:ssZ",
      "status": "submitted | draft_created | manual_required | blocked | failed",
      "publish_job_id": "string",
      "risk_notes": ["string"]
    }
  ],
  "missing_configuration": ["string"],
  "next_node": "published | draft_created | human_review | blocked_setup | qa_review"
}
```
