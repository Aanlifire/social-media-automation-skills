---
name: travel-video-asset-generation
description: Convert structured travel short-video script JSON into provider-agnostic asset-generation request JSON for video, image, TTS, map animation, UI card, overlay, and cover generation. Use when Codex or OpenClaw needs to prepare downstream media-generation jobs from a validated travel video script package for Douyin, Xiaohongshu, WeChat Channels, TikTok, or similar automated video workflows.
---

# Travel Video Asset Generation

Use this skill as the asset-planning node after scriptwriting. It converts a script package into deterministic request objects that downstream video, image, TTS, motion-graphics, and editing systems can execute.

This skill does not call media providers directly, does not render video, does not run FFmpeg, and does not publish content. It only prepares structured asset requests.

Read [references/input-contract.md](references/input-contract.md) before transforming the script package. Read [references/provider-rules.md](references/provider-rules.md) before writing prompts. Return JSON that conforms to [references/output-schema.md](references/output-schema.md).

## Core Workflow

1. Read the incoming script package and normalize:
   - platform
   - duration
   - story pattern
   - scenes
   - agent insertion
   - asset requests
   - TTS requests
2. Expand each scene into concrete generation tasks:
   - `video`
   - `image`
   - `tts`
   - `map_animation`
   - `ui_card`
   - `overlay`
   - `cover`
3. Rewrite prompts so they are:
   - visually explicit
   - safe for provider APIs
   - free of copyrighted character or celebrity dependence
   - stable enough for repeated generation
4. Add technical constraints for each task:
   - aspect ratio
   - target duration
   - camera motion guidance
   - composition
   - subtitle-safe area
   - branding-safe area
5. Identify which requests are reusable across videos:
   - destination establishing shots
   - itinerary UI cards
   - budget overlays
   - CTA end cards
6. Return only structured JSON. Do not wrap it in Markdown unless explicitly requested.

## Asset Strategy

Prefer the cheapest asset type that still solves the scene.

- Use `video` for establishing shots, moving city scenes, crowd contrast, and character action.
- Use `image` when motion is unnecessary or can be added later in editing.
- Use `map_animation` for route explanation.
- Use `ui_card` for itinerary, budget, and comparison displays.
- Use `overlay` for prices, bullets, labels, arrows, and warnings.
- Use `tts` for spoken narration.
- Use `cover` for platform thumbnail generation.

Do not ask for expensive generated video when a static image plus motion graphics can carry the idea.

## Prompt Rules

- Write prompts in concrete visual language.
- Include destination, time of day, mood, camera framing, and key action.
- Keep each prompt focused on one scene objective.
- Avoid provider-specific syntax unless the caller explicitly asks for one provider.
- Avoid celebrity likeness, copyrighted mascots, fake screenshots, and unverifiable real persons.
- Keep branding indirect unless the scene is a UI card or end card.

## TTS Rules

- Split long narration into manageable segments.
- Keep one segment aligned to one scene whenever possible.
- Mark the intended tone briefly, not poetically.
- Keep room for subtitle timing and mobile readability.

## Risk Handling

If a scene depends on a hard factual claim:

- preserve the structure
- mark `needs_fact_check: true`
- avoid baking uncertain numbers into image/video prompts

If a scene is visually weak:

- downgrade from `video` to `image` or `ui_card`
- note the reason in the output

If a request is redundant:

- mark it reusable instead of duplicating work

## Handoff

Set downstream hints for:

- `video_generation`
- `image_generation`
- `tts_generation`
- `graphics_generation`
- `editing`
- `fact_check`
