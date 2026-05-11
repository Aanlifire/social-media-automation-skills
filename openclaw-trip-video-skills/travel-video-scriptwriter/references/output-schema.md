# Output Schema

Return JSON only.

```json
{
  "status": "ok",
  "request": {
    "platform": "douyin | xiaohongshu | wechat_channels | tiktok | broad",
    "duration_seconds": 30,
    "brand_name": "string",
    "tone": "direct | friendly | sharp | checklist"
  },
  "assumptions": ["string"],
  "script_package": {
    "title_variants": ["string"],
    "cover_text_variants": ["string"],
    "caption_variants": ["string"],
    "hashtags": ["string"],
    "hook": "string",
    "summary": "string",
    "needs_fact_check": false,
    "story_pattern": "pitfall | budget_compare | route_optimization | ai_plans_my_trip | reverse_story | comment_to_plan",
    "scenes": [
      {
        "scene_id": "scene-01",
        "start_sec": 0,
        "end_sec": 3,
        "purpose": "hook | conflict | reveal | cta",
        "visual_prompt": "string",
        "voiceover": "string",
        "subtitle": "string",
        "onscreen_text": "string",
        "editing_notes": ["string"]
      }
    ],
    "agent_insert": {
      "placement": "midroll | endcard | both",
      "line": "string",
      "cta": "string"
    },
    "asset_requests": [
      {
        "type": "video | image | map_animation | ui_card | overlay",
        "purpose": "string",
        "prompt": "string"
      }
    ],
    "tts_requests": [
      {
        "voice_style": "string",
        "text": "string"
      }
    ],
    "next_nodes": ["asset_generation", "tts", "editing"]
  }
}
```

## Scene Guidance

- Keep scene timing stable and contiguous.
- Prefer 4-8 scenes for `30s`.
- Each `visual_prompt` should be concrete enough for image/video generation.
- `voiceover`, `subtitle`, and `onscreen_text` may differ slightly for readability.
