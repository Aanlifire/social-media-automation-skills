# Output Schema

Return JSON only.

```json
{
  "status": "ok | blocked | partial | failed",
  "missing_configuration": ["string"],
  "stored_assets": [
    {
      "asset_id": "asset-001",
      "type": "video | image | audio | subtitle | manifest | cover | final_video",
      "source": "string",
      "bucket": "string",
      "object_key": "string",
      "public_url": "string",
      "mime_type": "string",
      "status": "uploaded | pending_upload | failed",
      "error": "string"
    }
  ],
  "next_node": "editing_plan | qa_review | publisher | human_setup_required"
}
```
