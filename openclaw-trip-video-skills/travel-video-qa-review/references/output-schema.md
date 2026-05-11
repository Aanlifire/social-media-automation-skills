# Output Schema

Return JSON only.

```json
{
  "status": "ok",
  "decision": "approve | needs_repair | needs_fact_check | human_review_required | reject",
  "media_review_limited": false,
  "summary": "string",
  "risk_scores": {
    "factual": 0,
    "script_coherence": 0,
    "advertising": 0,
    "media_readiness": 0,
    "platform": 0,
    "brand": 0,
    "overall": 0
  },
  "findings": [
    {
      "id": "qa-001",
      "severity": "blocker | high | medium | low",
      "category": "fact | script | asset | ad_insert | platform | brand | editing",
      "problem": "string",
      "evidence": "string",
      "repair_node": "topic_research | scriptwriter | asset_generation | editing | fact_check | human_review",
      "repair_instruction": "string"
    }
  ],
  "approved_elements": [
    "string"
  ],
  "next_node": "editing | fact_check | scriptwriter | asset_generation | human_review | publish_ready"
}
```

## Scoring

Use 0-10. Higher means more risk for all risk scores.

Default decision thresholds:

- `approve`: overall 0-2 and no blocker/high findings
- `needs_repair`: fixable medium/high issues without hard factual uncertainty
- `needs_fact_check`: any important unverified current fact
- `human_review_required`: brand, account, platform, legal, or ambiguous policy risk
- `reject`: blocker issue that cannot be repaired without changing the premise
