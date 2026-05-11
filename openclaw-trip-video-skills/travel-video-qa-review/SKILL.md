---
name: travel-video-qa-review
description: Review travel short-video production packages before publishing by checking factual risk, script consistency, asset readiness, ad-insertion quality, platform sensitivity, and whether human approval is required. Use when Codex or OpenClaw needs a QA gate for AI-generated travel videos, video drafts, captions, covers, or publishing packages.
metadata:
  openclaw:
    requires:
      llm: true
---

# Travel Video QA Review

Use this skill as the QA gate after scriptwriting, asset planning, rendering, or before publishing. It decides whether a travel short-video package can proceed, needs repair, needs fact check, or must wait for human review.

This skill does not publish content, operate accounts, render media, or run FFmpeg. It only reviews structured inputs and returns a decision with repair instructions.

Read [references/review-checklist.md](references/review-checklist.md) before judging a package. Return JSON that conforms to [references/output-schema.md].

## Inputs

Accept any combination of:

- topic research JSON
- script package JSON
- asset plan JSON
- rendered video metadata
- caption, title, cover text, hashtags
- source/evidence list
- platform target
- brand/agent insertion copy

If the actual video file is unavailable, review the structured package and mark `media_review_limited: true`.

## Core Workflow

1. Normalize the package:
   - platform
   - destination
   - audience
   - claims
   - CTA
   - source evidence
   - scene list
   - asset list
2. Check factual risk:
   - current prices
   - opening hours
   - route closures
   - transport changes
   - weather
   - visa or entry rules
   - safety alerts
3. Check script coherence:
   - hook matches topic
   - scenes are ordered
   - voiceover, subtitle, and on-screen text do not conflict
   - CTA is clear
4. Check advertising quality:
   - agent insertion is natural
   - claims are not exaggerated
   - no fake scarcity or fake guarantee
   - brand appears at sensible moments
5. Check media readiness:
   - all required assets are present or requested
   - timing is plausible
   - text can fit mobile vertical video
   - cover text is short enough
6. Check platform and safety risk:
   - misleading claims
   - sensitive events
   - medical or safety certainty
   - impersonation or copyrighted likeness
   - account automation risk if publishing is included
7. Return one decision:
   - `approve`
   - `needs_repair`
   - `needs_fact_check`
   - `human_review_required`
   - `reject`

## Decision Rules

Use `approve` only when the package is coherent, low-risk, and does not depend on unverified current facts.

Use `needs_repair` when the problem is fixable by script, asset, caption, or CTA changes.

Use `needs_fact_check` when hard facts remain and evidence is missing or stale.

Use `human_review_required` when the package may be publishable but has brand, compliance, platform, or account-risk implications.

Use `reject` when the idea is fundamentally unsafe, misleading, or not aligned with the travel-planning agent.

## Repair Handoff

Route repairs to:

- `topic_research`
- `scriptwriter`
- `asset_generation`
- `editing`
- `fact_check`
- `human_review`

Keep repair instructions short, concrete, and assignable to one downstream node whenever possible.
