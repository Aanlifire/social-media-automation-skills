---
name: travel-video-scriptwriter
description: Write structured short-video scripts, hooks, story beats, voiceover lines, subtitle drafts, asset prompts, and agent-insertion copy for a travel-planning agent. Use when Codex or OpenClaw needs to convert topic-research output into production-ready script JSON for Douyin, Xiaohongshu, WeChat Channels, TikTok, or similar travel short-video workflows.
metadata:
  openclaw:
    requires:
      llm: true
---

# Travel Video Scriptwriter

Use this skill as the scriptwriting node after topic research. It converts a validated topic into a production-ready short-video script package for AI video generation, TTS, subtitle timing, and template-based editing.

This skill should not search the web unless the caller explicitly asks for fact repair, should not render media, should not call FFmpeg, and should not publish content. It only produces structured writing outputs for downstream nodes.

## Input Expectations

Prefer structured input from the topic-research node. At minimum, expect:

- title
- destination
- audience
- pain_point
- content_angle
- video_hook
- agent_insert
- risk_notes

If the caller provides only a rough idea, normalize it into the same fields before writing.

## Core Workflow

1. Read `references/input-contract.md` to understand expected fields.
2. Identify:
   - platform
   - duration target
   - audience sophistication
   - emotional trigger
   - travel-planning-agent role
3. Choose a script pattern:
   - pitfall
   - budget compare
   - route optimization
   - AI plans my trip
   - reverse story
   - comment to plan
4. Write a concise hook for the first 1-3 seconds.
5. Expand into scene-by-scene beats with:
   - on-screen goal
   - voiceover
   - subtitle line
   - visual prompt
   - editing notes
6. Insert the travel-planning agent naturally:
   - midroll explanation
   - endcard CTA
7. Produce title variants, caption variants, and hashtag suggestions.
8. Return valid JSON only, following `references/output-schema.md`.

## Writing Rules

Read `references/writing-rules.md` before writing final output.

Apply these defaults:

- Start with conflict, not explanation.
- Prefer one sharp pain point over broad tourism description.
- Keep spoken lines short and natural.
- Make each scene visually obvious enough for AI-generated footage or motion graphics.
- Mention the agent as the solution to the travel-planning problem, not as a generic ad.
- End with one clear CTA.

## Duration Rules

Default durations:

- `15s`: fast hook, one conflict, one reveal, one CTA
- `30s`: hook, conflict, explanation, reveal, CTA
- `45s`: only when the topic genuinely needs comparison or mini-story progression

Do not pad scripts. If the idea is thin, keep it shorter.

## Platform Rules

- `douyin`: strong hook, fast cuts, direct wording, high contrast between wrong and right route
- `xiaohongshu`: more lifestyle framing, clearer budgeting and checklist feel
- `wechat_channels`: slightly more explanatory, still concise
- `tiktok`: globally understandable framing, avoid niche mainland phrasing unless requested

## Risk Handling

If the topic includes current prices, opening hours, safety alerts, visa rules, weather, or public event details:

- keep the copy high-level
- avoid hard factual numbers unless verified
- set `needs_fact_check: true`

If the topic evidence is weak:

- shift toward evergreen framing
- remove overly specific claims
- keep the pain point and planning value

## Handoff

Set downstream hints for:

- `asset_generation`
- `tts`
- `editing`
- `fact_check`

Use `fact_check` when hard claims remain in the copy.
