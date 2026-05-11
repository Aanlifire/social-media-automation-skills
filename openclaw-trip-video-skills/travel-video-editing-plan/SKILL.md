---
name: travel-video-editing-plan
description: Convert generated travel video assets, TTS files, subtitles, overlays, map animations, UI cards, and brand inserts into deterministic editing and render specifications for Remotion, FFmpeg, or a video-worker service. Use when Codex or OpenClaw needs a timeline plan, render manifest, asset validation checklist, or handoff JSON for automated travel short-video production.
metadata:
  openclaw:
    requires:
      llm: true
---

# Travel Video Editing Plan

Use this skill after asset generation and before deterministic rendering. It converts script and asset outputs into a render manifest that a static worker can execute.

This skill does not run FFmpeg, render video, download files, or publish content. It prepares deterministic editing specifications for downstream scripts or services.

Read [references/render-contract.md](references/render-contract.md) before output. Return JSON that follows [references/output-schema.md].

## Core Workflow

1. Normalize inputs:
   - script scenes
   - generated video/image assets
   - TTS audio
   - subtitles
   - overlays
   - map animations
   - brand inserts
2. Validate timeline:
   - scene order
   - contiguous timing
   - total duration
   - audio coverage
   - subtitle alignment
3. Choose editing template:
   - pitfall
   - budget compare
   - route optimization
   - AI plans my trip
   - comment to plan
4. Build render manifest:
   - aspect ratio
   - resolution
   - frame rate
   - scene layers
   - audio tracks
   - subtitle tracks
   - safe areas
   - cover export frame
5. Mark missing or risky assets.
6. Return a deterministic handoff for Remotion, FFmpeg, or video-worker.

## Determinism Rules

- Do not invent file paths.
- Do not write raw FFmpeg shell commands unless explicitly requested.
- Prefer structured render parameters over free-form instructions.
- Keep all timing in seconds.
- Use stable IDs for scenes, layers, and assets.
- Route missing assets back to `asset_generation`.

## Template Guidance

- `pitfall`: fast hook, wrong-route contrast, corrected route reveal, CTA.
- `budget_compare`: split-screen or alternating cost cards.
- `route_optimization`: map layer plus itinerary cards.
- `ai_plans_my_trip`: UI card reveal plus travel montage.
- `comment_to_plan`: comment prompt, generated plan card, CTA.

## Handoff

Set `next_node` to:

- `render_worker`
- `asset_generation`
- `tts_generation`
- `qa_review`

Use `qa_review` only after render inputs are complete.
