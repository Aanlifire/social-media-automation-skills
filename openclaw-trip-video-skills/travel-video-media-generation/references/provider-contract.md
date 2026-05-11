# Provider Contract

Provider adapters should normalize all media generation results into the same shape.

## Environment Keys

Use provider-specific keys outside the skill content. Examples:

- `IMAGE_PROVIDER`
- `VIDEO_PROVIDER`
- `TTS_PROVIDER`
- `MEDIA_WORKER_ENDPOINT`
- `MEDIA_WORKER_TOKEN`
- `OSS_BUCKET`

## Required Result Fields

- request ID
- provider
- provider task ID
- status
- local path or remote URI
- duration for audio/video
- width and height for image/video
- retryable flag
- error message if failed

## Provider Modes

- `sync`: provider returns file immediately.
- `async`: provider returns task ID and requires polling.
- `worker`: local service handles provider-specific calls.
- `pending_provider`: no provider configured.

## Failure Policy

Transient errors should be retryable. Policy, content-safety, missing-credential, and invalid-prompt errors should not be retried blindly.
