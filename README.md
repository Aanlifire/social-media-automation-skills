# Social Media Automation Skills

OpenClaw/Codex-style skills for social content workflows and AI travel short-video automation.

This repository contains two complementary skill sets:

- `social-content-studio`: turns fragmented creator notes, transcripts, chats, and half-finished drafts into review-ready social media content packages.
- `openclaw-trip-video-skills`: provides an end-to-end travel short-video workflow for topic research, scriptwriting, brand insertion, asset planning, media generation, storage, fact-checking, editing plans, rendering, QA, and publishing handoff.

## Repository Layout

```text
social-content-studio/
  SKILL.md
  agents/
  references/

openclaw-trip-video-skills/
  README.md
  WORKFLOW.md
  .env.example
  workflow/
  travel-video-topic-research/
  travel-video-scriptwriter/
  travel-video-brand-insert/
  travel-video-asset-generation/
  travel-video-media-generation/
  travel-video-oss-storage/
  travel-video-fact-check/
  travel-video-editing-plan/
  travel-video-render-worker/
  travel-video-qa-review/
  travel-video-publisher/
```

## What Works Without External Services

You can use the skills for:

- creator note cleanup and social draft packaging
- idea clarification and argument structuring
- travel topic, script, asset, QA, and publishing handoff JSON
- local deterministic SVG placeholder generation
- upload manifest creation
- dry-run storage and manual-queue publishing packages

## Full Automation Requirements

The short-video workflow is designed to connect to real execution services. For complete automated video generation and publishing, configure:

- a media provider such as DashScope for AI video, image, and TTS generation
- FFmpeg, Remotion, or a remote render worker for final MP4 and cover rendering
- Alibaba Cloud OSS or compatible object storage
- official platform API access, a draft-queue service, or a custom publisher endpoint

See `openclaw-trip-video-skills/.env.example` and `openclaw-trip-video-skills/WORKFLOW.md`.

## Installation

Copy the skill folders you need into your OpenClaw/Codex skills directory, or install this repository using the deployment method supported by your runtime.

For text and draft workflows, install:

```text
social-content-studio/
```

For the travel short-video workflow, install the skill folders inside:

```text
openclaw-trip-video-skills/
```

## Safety Notes

- Do not commit real `.env` files or provider credentials.
- Keep platform tokens, OSS keys, and media provider keys in your runtime environment.
- Generated media, render output, logs, and upload artifacts are ignored by Git.

## License

MIT
