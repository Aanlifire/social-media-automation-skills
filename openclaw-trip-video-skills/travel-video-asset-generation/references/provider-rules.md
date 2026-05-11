# Provider Rules

Keep asset requests provider-agnostic unless the caller explicitly asks for a named provider.

## General Prompting

- Prefer one visual objective per request.
- Specify subject, setting, framing, motion, and mood.
- Keep prompts short enough to be portable across vendors.
- Avoid dense narrative prompts for a single shot.

## Video Requests

Use for:

- city establishing shots
- travel movement
- crowd contrast
- emotional reaction
- food or attraction montage with motion

Include:

- duration target
- aspect ratio
- shot framing
- motion type
- scene purpose

## Image Requests

Use for:

- hero stills
- destination cards
- fallback visual plates
- stylized travel concepts

## TTS Requests

- Keep segments short.
- Prefer natural spoken cadence.
- Match tone to platform and audience.

## Graphics Requests

Use `map_animation`, `ui_card`, and `overlay` for deterministic scenes.

Prefer deterministic graphics when:

- the point is route logic
- the point is budget comparison
- the point is itinerary structure
- generated footage adds cost without clarity
