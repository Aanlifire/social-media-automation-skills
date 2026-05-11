---
name: travel-video-brand-insert
description: Add natural brand mentions, CTA lines, end cards, overlays, and conversion prompts to travel short-video scripts for an AI travel-planning agent without making the content feel like a hard ad. Use when Codex or OpenClaw needs to adapt a travel video script, caption, cover, or editing package for soft promotion, comment leads, brand recall, or agent conversion.
metadata:
  openclaw:
    requires:
      llm: true
---

# Travel Video Brand Insert

Use this skill after topic research or scriptwriting, and before asset generation or QA. It inserts the travel-planning agent into the content as a useful solution, not as a generic advertisement.

This skill does not search, render media, publish content, or operate accounts. It only rewrites or enriches copy and structured script fields.

Read [references/brand-policy.md](references/brand-policy.md) before writing. Return JSON that follows [references/output-schema.md].

## Core Workflow

1. Normalize the incoming script or topic package:
   - brand name
   - agent value proposition
   - platform
   - audience
   - scene list
   - current CTA
2. Choose insertion points:
   - midroll line
   - endcard CTA
   - corner watermark text
   - cover subtitle
   - caption CTA
   - comment prompt
3. Rewrite the insertion so it solves the viewer's problem:
   - route optimization
   - budget planning
   - trip duration planning
   - avoiding detours
   - comparing itinerary options
4. Remove hard-sell claims, guarantees, fake urgency, and exaggerated savings claims.
5. Return structured copy variants and downstream editing hints.

## Insertion Rules

- Keep the first 3 seconds focused on the viewer's pain point.
- Put the first brand mention after the problem is clear.
- Use one clear CTA at the end.
- Keep brand lines short enough for vertical video overlays.
- Prefer "input city, days, budget" over abstract AI claims.
- Do not invent product capabilities that the travel agent does not have.

## Default CTA Patterns

Use patterns like:

- "Input city, days, and budget. Let the AI arrange the route."
- "Want the same route? Use the planner to generate your version."
- "Comment city + days + budget, then generate a full route with the planner."

Avoid:

- "Use it now or miss out"
- "Guaranteed to save money"
- "The best travel planner"
- "Everyone is using it"

## Handoff

Set `next_node` to:

- `scriptwriter` if script structure changed
- `asset_generation` if only overlay/endcard/caption assets are needed
- `qa_review` if the package is ready for review
