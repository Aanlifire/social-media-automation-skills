# Review Gates

This workflow is designed for cloud execution with human approvals at the points that most affect quality, cost, or publishing risk.

## Default Gates

### 1. Topic Review

State: `HUMAN_TOPIC_REVIEW`

Approve only when:
- one topic candidate is clearly selected
- the target platform is clear
- the hook is specific enough for a short video
- evidence and source notes are sufficient for the claim type
- there is no obvious safety, policy, or account-risk issue

If the topic is weak, choose `revise` and send notes back to `TOPIC_PENDING`.

### 2. Script Review

State: `HUMAN_SCRIPT_REVIEW`

Approve only when:
- the first 3 seconds have a clear hook
- the storyline is understandable without extra context
- the brand insertion feels natural
- CTA, overlays, and comment prompts do not turn the video into a hard ad
- uncertain prices, opening hours, transport claims, or safety claims are marked for fact check

If the story direction is wrong, choose `revise` and send notes back to `SCRIPT_PENDING`.

### 3. Asset Plan Review

State: `HUMAN_ASSET_PLAN_REVIEW`

Approve only when:
- each generated asset has a clear purpose
- costly video generation is used only when motion matters
- UI cards, overlays, map animations, TTS, and cover assets are planned
- prompts are concrete and provider-safe
- subtitle-safe and brand-safe areas are considered

This gate prevents wasting media-provider credits on weak scripts or unnecessary video generation.

### 4. Publish Review

State: `HUMAN_PUBLISH_REVIEW`

Approve only when:
- the final MP4 and cover are available
- QA has approved the package or all review notes have been accepted
- title, caption, hashtags, and cover text fit the target platform
- factual, safety, and account-risk issues are resolved

If the package is not ready, choose `revise` and send notes back to `QA_READY`.

## Approval Events

Use these event names consistently in OpenClaw or your task runner:

```text
approve -> continue
revise  -> return to the configured repair state
reject  -> stop as REJECTED
```

Human review notes should be attached to the workflow state so the next skill can repair the package instead of starting from scratch.
