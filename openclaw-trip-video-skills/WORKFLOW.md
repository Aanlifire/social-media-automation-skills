# End-to-End Workflow

This repository now contains both workflow skills and execution helpers.

## Full Path

```text
topic research
-> human topic review
-> scriptwriting
-> brand insert
-> human script review
-> asset request planning
-> human asset plan review
-> media generation
-> OSS storage
-> fact check
-> editing plan
-> render worker
-> OSS storage
-> QA review
-> human publish review
-> publishing
```

## Cloud Production Mode

The default OpenClaw workflow is intended to be plug-and-play as a supervised production line:

1. OpenClaw generates topic candidates.
2. The workflow pauses at `HUMAN_TOPIC_REVIEW`.
3. After approval, OpenClaw writes the script and brand insertion.
4. The workflow pauses at `HUMAN_SCRIPT_REVIEW`.
5. After approval, OpenClaw creates the asset plan.
6. The workflow pauses at `HUMAN_ASSET_PLAN_REVIEW` before paid media generation.
7. After approval, OpenClaw generates assets, stores media, fact-checks, plans editing, renders, stores final output, and runs QA.
8. The workflow pauses at `HUMAN_PUBLISH_REVIEW`.
9. After approval, OpenClaw creates platform publish jobs or a manual queue package.

Use `approve`, `revise`, and `reject` as the human-review events. See `workflow/review-gates.md` for approval criteria.

## Runtime Requirements

The skills are runnable workflow nodes, but external execution still needs real credentials or binaries:

- DashScope API key for Wan image/video and Qwen TTS generation.
- `ossutil` plus OSS bucket configuration for Alibaba Cloud OSS uploads.
- FFmpeg or a render worker endpoint for final MP4 rendering.
- Official platform API, draft queue, or manual queue endpoint for publishing.

## Local Script Smoke Tests

Create media jobs from an asset plan:

```powershell
python travel-video-media-generation/scripts/dispatch_media_jobs.py examples/local-ui-card-asset-plan.json output/media-jobs.json
```

Generate local deterministic SVG assets:

```powershell
python travel-video-media-generation/scripts/dashscope_media_worker.py output/media-jobs.json output/media-results.json --output-dir output/media
```

Build OSS upload manifest for generated media assets:

```powershell
python travel-video-oss-storage/scripts/build_upload_manifest.py output/media-results.json demo-video-001 output/upload-manifest.json
```

Upload generated media assets, or leave them in pending-upload state:

```powershell
python travel-video-oss-storage/scripts/ossutil_upload.py output/upload-manifest.json output/storage-result.json --dry-run
```

Build OSS upload manifest for final render output. Render outputs are routed to QA by default:

```powershell
python travel-video-oss-storage/scripts/build_upload_manifest.py output/render-result.json demo-video-001 output/final-upload-manifest.json
python travel-video-oss-storage/scripts/ossutil_upload.py output/final-upload-manifest.json output/final-storage-result.json --dry-run
```

Create publish package:

```powershell
python travel-video-publisher/scripts/create_publish_package.py examples/approved-package.json output/publish-jobs.json
```

Submit publish package to a configured endpoint, or generate manual queue output:

```powershell
python travel-video-publisher/scripts/http_publish_worker.py output/publish-jobs.json output/publish-result.json --dry-run
```
