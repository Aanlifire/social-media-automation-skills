# Output Schema

Return JSON only.

```json
{
  "status": "ok",
  "brand_insert_package": {
    "brand_name": "string",
    "platform": "douyin | xiaohongshu | wechat_channels | tiktok | broad",
    "midroll_lines": ["string"],
    "endcard_ctas": ["string"],
    "caption_ctas": ["string"],
    "comment_prompts": ["string"],
    "overlay_text": ["string"],
    "watermark_text": "string",
    "scene_updates": [
      {
        "scene_id": "scene-01",
        "field": "voiceover | subtitle | onscreen_text | editing_notes",
        "replacement": "string",
        "reason": "string"
      }
    ],
    "claims_removed": ["string"],
    "risk_notes": ["string"],
    "next_node": "scriptwriter | asset_generation | qa_review"
  }
}
```
