---
name: travel-video-media-generation
description: Execute or dispatch travel video media generation jobs for AI images, AI videos, TTS audio, subtitle timing, covers, UI cards, overlays, and map animation assets from an asset plan. Use when Codex or OpenClaw needs to turn asset request JSON into concrete media job records, provider task IDs, generated file URIs, retryable failures, or object-storage-ready artifacts.
metadata:
  openclaw:
    requires:
      imageGeneration: true
      videoGeneration: true
      textToSpeech: true
---

# Travel Video Media Generation

Use this skill after `travel-video-asset-generation`. It converts asset requests into executable provider jobs and returns media results that downstream storage and render nodes can consume.

This skill is the media-generation bridge. It may call configured provider tools or dispatch jobs to a media worker. It must not invent successful asset URLs when a provider has not returned them.

Read [references/provider-contract.md](references/provider-contract.md) before execution. Return JSON matching [references/output-schema.md].

## Core Workflow

1. Read the asset plan.
2. Group requests by type:
   - image
   - video
   - tts
   - cover
   - ui_card
   - overlay
   - map_animation
3. For each request, choose execution mode:
   - direct provider call if OpenClaw exposes a tool
   - media-worker dispatch if an endpoint is configured
   - `pending_provider` if no executable provider exists
4. Submit jobs with stable IDs.
5. Poll async jobs only when the provider contract supports polling.
6. Return provider task IDs, local file paths, object storage candidates, durations, and failures.
7. Route incomplete items back to retry or human setup.

## Execution Rules

- Never mark an asset as generated without a real provider response or existing file.
- Preserve request IDs from the asset plan.
- Add retry metadata for transient provider failures.
- Keep generated media separate from rendered final videos.
- If provider credentials are missing, return `status: "blocked"` with exact missing environment keys.
- If only prompts are available, return dispatchable jobs, not fake results.

## Handoff

Set `next_node` to:

- `oss_storage` when files exist and need upload.
- `editing_plan` when media URLs are already available.
- `asset_generation` when prompts are invalid or incomplete.
- `human_setup_required` when no provider is configured.
