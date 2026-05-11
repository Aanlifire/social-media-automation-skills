---
name: travel-video-render-worker
description: Execute or dispatch deterministic rendering of final travel short videos from render manifests, generated assets, TTS audio, subtitles, covers, overlays, and brand elements. Use when Codex or OpenClaw needs to create final MP4 files, covers, subtitle files, render job records, or video-worker tasks from a validated editing plan.
metadata:
  openclaw:
    requires:
      videoRender: true
      ffmpeg: true
---

# Travel Video Render Worker

Use this skill after `travel-video-editing-plan`. It prepares and dispatches render jobs for deterministic code such as Remotion, FFmpeg, or a configured video-worker service.

This skill may run bundled validation scripts or dispatch to a render worker. It should not alter the creative script. If a renderer is not configured, return a blocked render job with the missing setup.

Read [references/render-worker-contract.md](references/render-worker-contract.md). Return JSON matching [references/output-schema.md].

## Core Workflow

1. Read render manifest.
2. Validate:
   - scene timing
   - asset URIs
   - audio coverage
   - subtitle timing
   - export settings
3. Choose render mode:
   - Remotion worker
   - FFmpeg worker
   - remote video-worker endpoint
   - blocked until renderer setup
4. Dispatch render job with stable ID.
5. Return final file path, cover path, logs, or error.

## Deterministic Rules

- Do not modify copy, claims, or scene ordering.
- Do not guess missing file paths.
- Do not mark `rendered` until a final MP4 exists.
- Keep render logs separate from user-facing captions.
- Route missing assets back to `media_generation` or `oss_storage`.

## Handoff

Set `next_node` to:

- `oss_storage` when a local final MP4 exists.
- `qa_review` when the rendered video already has a storage URL.
- `editing_plan` when manifest structure is invalid.
- `human_setup_required` when no renderer is configured.
