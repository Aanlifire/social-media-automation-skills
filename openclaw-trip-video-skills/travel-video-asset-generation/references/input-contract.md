# Input Contract

Expect normalized script JSON from the scriptwriter node.

```json
{
  "request": {
    "platform": "douyin",
    "duration_seconds": 30,
    "brand_name": "string",
    "tone": "direct"
  },
  "script_package": {
    "title_variants": ["string"],
    "hook": "string",
    "needs_fact_check": false,
    "story_pattern": "pitfall",
    "scenes": [
      {
        "scene_id": "scene-01",
        "start_sec": 0,
        "end_sec": 3,
        "purpose": "hook",
        "visual_prompt": "string",
        "voiceover": "string",
        "subtitle": "string",
        "onscreen_text": "string",
        "editing_notes": ["string"]
      }
    ],
    "agent_insert": {
      "placement": "midroll",
      "line": "string",
      "cta": "string"
    },
    "asset_requests": [
      {
        "type": "video",
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

If fields are missing, infer conservatively and record assumptions.
