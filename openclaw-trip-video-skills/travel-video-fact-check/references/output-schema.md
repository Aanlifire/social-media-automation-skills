# Output Schema

Return JSON only.

```json
{
  "status": "ok",
  "overall_decision": "verified | needs_rewrite | needs_more_evidence | human_review_required | reject",
  "checked_at": "YYYY-MM-DDTHH:mm:ssZ",
  "claims": [
    {
      "claim_id": "claim-001",
      "claim": "string",
      "claim_type": "evergreen | current | high_risk_current | subjective | promotional",
      "decision": "verified | partially_verified | unsupported | contradicted | needs_rewrite",
      "evidence": [
        {
          "source_level": "P0 | P1 | P2 | P3",
          "title": "string",
          "url": "string",
          "date_context": "string",
          "supports": true
        }
      ],
      "repair_instruction": "string"
    }
  ],
  "safe_rewrites": [
    {
      "original": "string",
      "replacement": "string",
      "reason": "string"
    }
  ],
  "next_node": "qa_review | scriptwriter | topic_research | human_review"
}
```
