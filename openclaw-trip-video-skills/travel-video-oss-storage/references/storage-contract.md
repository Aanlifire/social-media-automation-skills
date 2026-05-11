# Storage Contract

## Required Environment

For Alibaba Cloud OSS, the runtime or worker should provide:

- `OSS_ENDPOINT`
- `OSS_BUCKET`
- `OSS_ACCESS_KEY_ID`
- `OSS_ACCESS_KEY_SECRET`
- optional `OSS_PUBLIC_BASE_URL`

## Object Key Pattern

```text
trip-video/{yyyy}/{mm}/{dd}/{video_id}/{asset_type}/{asset_id}.{ext}
```

Final renders:

```text
trip-video/{yyyy}/{mm}/{dd}/{video_id}/final/video.mp4
trip-video/{yyyy}/{mm}/{dd}/{video_id}/final/cover.jpg
trip-video/{yyyy}/{mm}/{dd}/{video_id}/final/caption.txt
```

## Upload Policy

- Use idempotent keys.
- Validate file exists before upload.
- Keep MIME type.
- Return public URL only when configured.
- Otherwise return bucket and object key.
- `--dry-run` is allowed without OSS credentials and leaves records in `pending_upload`.
- Route generated media assets to `editing_plan`.
- Route final rendered video and cover outputs to `qa_review`.
- Use `--next-node publisher` only for already approved final assets.
