# Input Contract

This skill works best with normalized topic JSON from the research node.

Expected input shape:

```json
{
  "title": "string",
  "destination": "string",
  "audience": "string",
  "platform_fit": ["douyin"],
  "content_angle": "pitfall | budget_compare | route_optimization | ai_plans_my_trip | reverse_story | comment_to_plan",
  "pain_point": "string",
  "video_hook": "string",
  "agent_insert": {
    "placement": "midroll | endcard | both",
    "line": "string",
    "cta": "string"
  },
  "risk_notes": ["string"]
}
```

Optional caller fields:

- `duration_seconds`
- `platform`
- `brand_name`
- `brand_claims`
- `tone`
- `must_include`
- `must_avoid`

If fields are missing, infer conservatively and note assumptions in the output.
