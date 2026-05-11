# OpenClaw Trip Video Skills

A set of OpenClaw/Codex-style skills and helper scripts for an AI travel short-video production workflow.

This repository provides the workflow layer and local execution helpers. It does not ship provider credentials, FFmpeg binaries, object-storage credentials, or official platform publishing access. To run the full automated path, configure the runtime dependencies listed below.

## Skills

- `travel-video-topic-research`: discovers evidence-backed travel short-video topics from search signals.
- `travel-video-scriptwriter`: converts selected topics into structured short-video script JSON.
- `travel-video-brand-insert`: adds natural brand mentions, CTA lines, overlays, and comment prompts without turning the content into a hard ad.
- `travel-video-asset-generation`: converts scripts into provider-agnostic image, video, TTS, UI card, map, overlay, and cover asset requests.
- `travel-video-media-generation`: executes or dispatches image, video, TTS, cover, UI card, overlay, and map-animation generation jobs. Includes a DashScope/Wan/Qwen HTTP worker script.
- `travel-video-oss-storage`: prepares object-storage upload manifests and OSS handoff for generated assets and final renders. Includes an `ossutil` upload worker script.
- `travel-video-fact-check`: verifies travel claims such as prices, opening hours, reservations, transport changes, safety alerts, and current destination facts.
- `travel-video-editing-plan`: converts generated assets into a deterministic timeline and render manifest for Remotion, FFmpeg, or a video-worker service.
- `travel-video-render-worker`: executes or dispatches deterministic rendering into final MP4, cover, and render logs. Includes an FFmpeg fallback renderer.
- `travel-video-qa-review`: reviews scripts, asset plans, captions, covers, and publishing packages before release.
- `travel-video-publisher`: creates official API, draft queue, or manual queue publishing jobs for approved final videos. Includes an HTTP publisher worker and manual queue fallback.

## Intended Workflow

```text
travel-video-topic-research
  -> travel-video-scriptwriter
  -> travel-video-brand-insert
  -> travel-video-asset-generation
  -> travel-video-media-generation
  -> travel-video-oss-storage
  -> travel-video-fact-check
  -> travel-video-editing-plan
  -> travel-video-render-worker
  -> travel-video-oss-storage
  -> travel-video-qa-review
  -> human review when required
  -> travel-video-publisher
```

## What Works Out of the Box

Without any external API keys, you can:

- install and invoke the workflow skills
- create script, asset, render, QA, and publishing handoff JSON
- convert asset plans into media job records
- generate deterministic local SVG placeholders for UI cards, overlays, and map animations
- build OSS upload manifests
- create manual-queue publishing packages
- run dry-run storage and publisher smoke tests

## Runtime Requirements for Full Automation

To generate and publish real videos end to end, provide these dependencies:

- DashScope or another media provider for AI video, image, and TTS generation
- FFmpeg, Remotion, or a remote render worker for final MP4 and cover rendering
- Alibaba Cloud OSS or compatible object storage for generated assets and final renders
- official platform API access, a draft-queue service, or a custom publisher endpoint
- an OpenClaw/Codex runtime that can install and invoke these skill folders

Copy `.env.example` to `.env` or export equivalent environment variables in your runtime. Keep real secrets out of Git.

## Capability Levels

```text
Level 1: workflow skills for topic, script, asset planning, QA, and publish handoff
Level 2: media generation jobs and local SVG placeholders
Level 3: provider-backed AI images, video, and TTS
Level 4: FFmpeg/worker rendering into final MP4 and cover
Level 5: OSS upload and platform publishing or draft creation
```

## OpenClaw Deployment

Copy each skill folder into the OpenClaw skills directory or install this repository using the deployment method supported by your OpenClaw instance.

Each skill has:

```text
SKILL.md
agents/openai.yaml
references/
```

## Local Smoke Tests

See [WORKFLOW.md](WORKFLOW.md) for local script smoke tests. The smoke tests can run without provider credentials when using local SVG placeholders and `--dry-run` upload/publish commands.

## Notes

These skills define the full OpenClaw workflow layer. Provider-specific media generation, object-storage upload, rendering, and publishing require the matching runtime tools, API keys, or worker endpoints declared in each skill's references.
