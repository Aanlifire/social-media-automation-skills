# Render Contract

The editing plan should be executable by deterministic code.

## Required Concepts

- timeline
- scene
- layer
- asset
- audio track
- subtitle track
- overlay
- safe area
- export settings

## Render Defaults

- aspect ratio: 9:16
- resolution: 1080x1920
- frame rate: 30
- subtitle safe area: lower middle, above platform UI
- brand safe area: top corner or end card

## Asset Validation

Each asset should have:

- asset ID
- type
- URI or placeholder ID
- intended scene
- duration if time-based
- fallback instruction

Missing URI means the manifest is not render-ready.
