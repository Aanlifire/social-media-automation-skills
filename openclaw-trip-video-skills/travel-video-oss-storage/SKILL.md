---
name: travel-video-oss-storage
description: Prepare and execute object-storage handoff for generated travel video assets and final MP4 files, including OSS key planning, upload manifests, public/CDN URL mapping, retention metadata, and downstream render or publish references. Use when Codex or OpenClaw needs to persist AI-generated media, rendered videos, covers, subtitles, or publishing assets to Alibaba Cloud OSS or compatible object storage.
metadata:
  openclaw:
    requires:
      objectStorage: true
---

# Travel Video OSS Storage

Use this skill after media generation or final rendering. It turns local files or provider URLs into an object-storage manifest and, when an upload tool is configured, uploads them to OSS-compatible storage.

This skill must not fake uploaded URLs. If upload credentials or tools are missing, return a blocked manifest with exact missing setup.

Read [references/storage-contract.md](references/storage-contract.md). Return JSON matching [references/output-schema.md].

## Core Workflow

1. Read media results or rendered output.
2. Validate each file or remote URI.
3. Assign deterministic object keys:
   - project
   - date
   - video ID
   - asset type
   - request ID
4. Upload through configured OSS tool or create a pending upload manifest.
5. Return storage URLs and object metadata.
6. Route stored assets to editing, QA, or publisher.

The helper scripts preserve this routing through the upload manifest:
- media-generation results default to `next_node: editing_plan`
- render-worker results containing `final_video` or `cover` default to `next_node: qa_review`
- `ossutil_upload.py --next-node publisher` can be used for already approved final assets

## Key Rules

- Never overwrite final videos unless the job version matches.
- Keep raw generated assets separate from rendered outputs.
- Store captions, manifests, and covers beside the final MP4.
- Use stable object keys so retries are idempotent.
- Redact credentials from output.

## Handoff

Set `next_node` to:

- `editing_plan` for generated media assets.
- `qa_review` for rendered output.
- `publisher` for approved final videos.
- `human_setup_required` when storage is not configured.
