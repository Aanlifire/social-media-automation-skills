---
name: travel-video-fact-check
description: Verify factual claims in travel short-video topics, scripts, captions, cover text, and publishing packages using source triage and evidence grading. Use when Codex or OpenClaw needs to check prices, opening hours, reservations, transport changes, weather-sensitive claims, safety alerts, holiday rules, destination facts, or any current travel claim before video publishing.
metadata:
  openclaw:
    requires:
      webSearch: true
      webFetch: true
---

# Travel Video Fact Check

Use this skill when a travel video package contains factual or time-sensitive claims. It verifies claims, assigns evidence levels, and returns repair instructions for unsafe or unsupported statements.

This skill does not write full scripts, render media, publish content, or operate accounts. It only checks claims and returns structured verification output.

Read [references/source-policy.md](references/source-policy.md) before judging evidence. Return JSON that follows [references/output-schema.md].

## Core Workflow

1. Extract atomic claims from the package:
   - price
   - opening hours
   - ticketing or reservation rules
   - transport route or closure
   - weather or season claim
   - visa, entry, safety, or official-policy claim
   - destination popularity or trend claim
2. Classify each claim:
   - evergreen
   - current
   - high-risk current
   - subjective
   - promotional
3. Search and fetch evidence for current or high-risk claims.
4. Grade evidence:
   - P0 official
   - P1 authoritative
   - P2 community
   - P3 weak discovery signal
5. Decide:
   - verified
   - partially verified
   - unsupported
   - contradicted
   - needs rewrite
6. Return concrete repairs:
   - remove hard number
   - add date context
   - soften wording
   - route to human review

## Evidence Rules

- Use P0 for opening hours, closures, ticketing, entry rules, safety alerts, and official policy.
- Use P1 for broad trends or market context.
- Use P2 only for pain-point discovery or firsthand qualitative signals.
- Never treat search snippets as enough for hard facts.
- Add concrete dates for current claims.
- If evidence conflicts, prefer P0 and mark uncertainty.

## Rewrite Rules

Prefer safe wording:

- "recent reports suggest"
- "check the official page before departure"
- "prices can fluctuate"
- "reservation rules may change"

Avoid unsafe wording:

- exact current price without source
- guaranteed savings
- certain crowd predictions
- safety certainty
- official-rule claims without P0 support

## Handoff

Set `next_node` to:

- `qa_review` if all claims are safe
- `scriptwriter` if copy needs rewriting
- `topic_research` if the premise is unsupported
- `human_review` if risk remains ambiguous
