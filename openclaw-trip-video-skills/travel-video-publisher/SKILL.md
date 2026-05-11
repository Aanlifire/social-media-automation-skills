---
name: travel-video-publisher
description: Create or execute publishing jobs for approved travel short videos, including platform captions, titles, hashtags, cover selection, account safety checks, draft creation, official API publishing, and human-review handoff. Use when Codex or OpenClaw needs to prepare final approved MP4 assets for Douyin, Xiaohongshu, WeChat Channels, TikTok, or a manual publishing queue.
metadata:
  openclaw:
    requires:
      publishQueue: true
---

# Travel Video Publisher

Use this skill after QA approves a rendered and stored video. It creates platform-specific publish jobs or dispatches to a configured publisher service.

This skill must not bypass platform rules. Prefer official APIs, platform-approved integrations, or a human publishing queue. Do not rely on fragile cookie automation unless the user explicitly owns the account, accepts platform risk, and the workflow marks it as high risk.

Read [references/publish-contract.md](references/publish-contract.md). Return JSON matching [references/output-schema.md].

## Core Workflow

1. Read approved final video package:
   - final MP4 URL
   - cover URL
   - title
   - caption
   - hashtags
   - platform targets
   - QA decision
2. Confirm QA decision is `approve`.
3. Build platform-specific publish packages.
4. Choose publish mode:
   - official API
   - draft queue
   - manual review queue
   - blocked setup
5. Return publish job IDs, scheduled time, status, and platform risk notes.

## Safety Rules

- Do not publish if QA is not approved.
- Do not publish if fact check is unresolved.
- Do not publish if final MP4 URL is missing.
- Do not expose account tokens in output.
- Mark cookie/browser automation as high risk.

## Handoff

Set `next_node` to:

- `published`
- `draft_created`
- `human_review`
- `blocked_setup`
- `qa_review`
