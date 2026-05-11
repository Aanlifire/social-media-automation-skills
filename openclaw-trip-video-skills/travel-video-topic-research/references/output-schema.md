# Output Schema

Return JSON only. Use this shape for workflow consumption.

```json
{
  "status": "ok",
  "generated_at": "YYYY-MM-DDTHH:mm:ssZ",
  "request": {
    "audience": "students | couples | families | workers | first_time_travelers | broad",
    "destination_scope": "string",
    "time_window": "string",
    "platform": "douyin | xiaohongshu | wechat_channels | tiktok | broad",
    "content_goal": "followers | agent_conversion | comment_leads | brand_awareness",
    "output_count": 10
  },
  "query_plan": [
    {
      "query": "string",
      "intent": "trend | pain_point | fact_check | visual_angle | conversion_angle"
    }
  ],
  "topics": [
    {
      "id": "topic-001",
      "title": "string",
      "destination": "string",
      "audience": "string",
      "platform_fit": ["douyin", "xiaohongshu"],
      "content_angle": "pitfall | budget_compare | route_optimization | ai_plans_my_trip | reverse_story | comment_to_plan",
      "pain_point": "string",
      "video_hook": "string",
      "story_beats": [
        "0-3s hook",
        "3-12s conflict",
        "12-22s AI route/planning reveal",
        "22-30s CTA"
      ],
      "agent_insert": {
        "placement": "midroll | endcard | both",
        "line": "string",
        "cta": "string"
      },
      "visual_suggestions": [
        "AI city establishing shot",
        "map route animation",
        "budget comparison overlay"
      ],
      "evidence": [
        {
          "source_level": "P0 | P1 | P2 | P3",
          "title": "string",
          "url": "string",
          "used_for": "trend | fact | pain_point | visual_angle",
          "date_context": "string"
        }
      ],
      "scores": {
        "timeliness": 0,
        "pain_intensity": 0,
        "visual_potential": 0,
        "conversion_fit": 0,
        "evidence_quality": 0,
        "production_feasibility": 0,
        "risk": 0,
        "total": 0
      },
      "risk_notes": ["string"],
      "next_node": "scriptwriter | fact_check | skip_low_quality"
    }
  ],
  "discarded_clusters": [
    {
      "reason": "duplicate | weak_evidence | high_risk | low_conversion_fit",
      "examples": ["string"]
    }
  ]
}
```

## Scoring Guidance

Use 0-10 for every score.

- `timeliness`: recency and seasonal relevance.
- `pain_intensity`: how strongly the audience feels the problem.
- `visual_potential`: whether the idea can become clear scenes or overlays.
- `conversion_fit`: whether the AI travel-planning agent is a natural solution.
- `evidence_quality`: source tier, cross-checking, and specificity.
- `production_feasibility`: whether AI-generated visuals and templates can handle it.
- `risk`: higher means more risk.

Suggested total:

```text
total = timeliness * 1.2
      + pain_intensity * 1.4
      + visual_potential * 1.0
      + conversion_fit * 1.6
      + evidence_quality * 1.0
      + production_feasibility * 0.8
      - risk * 1.2
```

Round `total` to one decimal place.
