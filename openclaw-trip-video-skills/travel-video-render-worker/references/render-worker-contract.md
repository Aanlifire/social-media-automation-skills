# Render Worker Contract

## Runtime Inputs

- render manifest JSON
- asset URIs or local paths
- subtitle track
- audio track
- export settings

## Supported Render Modes

- `remotion`: React/Remotion renderer.
- `ffmpeg`: deterministic FFmpeg template.
- `remote_worker`: HTTP job service.
- `blocked`: renderer not configured.

## Environment Keys

- `RENDER_WORKER_ENDPOINT`
- `RENDER_WORKER_TOKEN`
- `REMOTION_PROJECT_DIR`
- `FFMPEG_PATH`
- `RENDER_OUTPUT_DIR`

## Success Criteria

- final MP4 exists
- duration is within accepted tolerance
- cover exists or cover export is explicitly skipped
- render log exists
