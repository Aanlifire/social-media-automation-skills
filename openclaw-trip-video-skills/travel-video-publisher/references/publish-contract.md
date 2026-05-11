# Publish Contract

## Required Input

- QA decision: `approve`
- final video URL or local path
- cover URL or local path
- title
- caption
- hashtags
- platform targets
- account or workspace identifier

## Publish Modes

- `official_api`: use official platform API.
- `draft_queue`: create a draft for human approval.
- `manual_queue`: output publish package only.
- `blocked_setup`: missing credentials or integration.

## Platform Risk

High-risk conditions:

- cookie automation
- private API reverse engineering
- unresolved fact check
- brand/legal ambiguity
- repeated duplicate uploads

Prefer draft or manual queue when risk is not clearly low.
