---
name: travel-video-topic-research
description: Research high-conversion travel short-video topics for an AI travel-planning agent using web search, source triage, pain-point extraction, trend scoring, and structured JSON output. Use when Codex or OpenClaw needs travel content ideas, destination trend discovery, short-video hooks, evidence-backed topic selection, or content angles for Douyin, Xiaohongshu, WeChat Channels, TikTok, or similar platforms.
metadata:
  openclaw:
    requires:
      webSearch: true
      webFetch: true
---

# Travel Video Topic Research

Use this skill as the topic-research node in a 7x24 travel-video production workflow. It turns web/search signals into evidence-backed short-video topics for promoting an AI travel-planning agent.

This skill should not render videos, write full scripts, call FFmpeg, publish posts, or operate accounts. It only produces ranked topic candidates and structured inputs for downstream scriptwriting and asset-generation nodes.

## Required Capabilities

Prefer available web search/fetch tools such as Brave Search. If web search is unavailable, say the skill cannot validate current trend evidence and produce only a clearly labeled offline brainstorm.

## Core Workflow

1. Normalize the request into:
   - target audience
   - destination scope
   - time window
   - platform
   - content goal
   - output count
2. Build a query plan with 8-20 searches. Cover:
   - destination + travel pitfalls
   - destination + budget
   - destination + itinerary duration
   - holiday/season + destination
   - family/couple/student/workers + destination
   - event/weather/transport/hotel/flight triggers
   - reverse tourism, crowding, local advisories, or common complaints
3. Search and fetch sources. Read enough context to support each selected topic.
4. Classify sources using `references/source-policy.md`.
5. Extract pain points and opportunities:
   - route-order mistakes
   - budget anxiety
   - overcrowding
   - transport friction
   - family or couple constraints
   - weather/season constraints
   - hidden local alternatives
   - high-intent planning needs
6. Cluster near-duplicate ideas. Keep the clearest topic from each cluster.
7. Score each candidate:
   - timeliness
   - pain intensity
   - visual potential
   - conversion fit for the travel-planning agent
   - evidence quality
   - production feasibility
   - risk
8. Return only structured JSON that conforms to `references/output-schema.md`, unless the user explicitly asks for an explanation.

## Topic Selection Rules

Prioritize topics that naturally create a need for the AI travel-planning agent:

- "route is easy to arrange wrong"
- "same trip, different route saves money/time"
- "first-timer pitfalls"
- "budget-specific itinerary"
- "family/couple/student constraints"
- "holiday crowd avoidance"
- "comment your city + days + budget"

Avoid topics that require unverifiable claims, medical/safety certainty, illegal scraping, fake reviews, impersonation, or misleading real-world prices.

## Evidence Rules

- Use P0/P1 evidence for time-sensitive or factual claims whenever possible.
- Never treat search snippets as enough for strong factual claims.
- Add concrete dates for current or seasonal claims.
- If evidence conflicts, prefer P0 over P1, P1 over P2, and state uncertainty in the output.
- Do not copy article titles or social-post wording as final hooks; rewrite them.

## Output Rules

Return valid JSON only. No Markdown wrapper unless requested.

Default `output_count` is 10. Each topic must include:

- topic title
- destination
- audience
- pain point
- video hook
- content angle
- agent insertion angle
- evidence list
- score object
- risk notes
- suggested next workflow node

Read `references/output-schema.md` before producing output if exact field names matter for automation.

## Failure Handling

If search fails:

- return `status: "search_unavailable"`
- include the query plan that would have been used
- include `offline_candidates` only if the user allows non-current ideation

If evidence is weak:

- keep the topic only when it is still useful as evergreen content
- mark `evidence_quality` below 5
- add `risk_notes`

If all topics are weak:

- return fewer topics rather than padding the list.

## Handoff

Set `next_node` to one of:

- `scriptwriter`
- `fact_check`
- `skip_low_quality`

Use `fact_check` for topics involving current prices, opening hours, route closures, weather, visa rules, safety alerts, or major public events.
