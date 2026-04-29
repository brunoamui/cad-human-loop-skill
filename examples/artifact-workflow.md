# Artifact workflow

This example shows how an agent should present progress while building a part.

The repo includes a helper that can generate these artifacts from the bundled examples:

```bash
python scripts/generate_checkpoints.py --module build123d --output-dir artifacts/build123d --stl
python scripts/generate_checkpoints.py --module cadquery --output-dir artifacts/cadquery --stl
```

## Suggested artifact directory

```text
artifacts/
  checkpoint-1-base.png
  checkpoint-1-base.step
  checkpoint-2-features.png
  checkpoint-2-features.step
  checkpoint-3-support.png
  checkpoint-3-support.step
  final.step
  final.stl
```

## Suggested checkpoint flow

### Checkpoint 1 — base shape
- build or update the base body
- render `checkpoint-1-base.png`
- export `checkpoint-1-base.step`
- summarize footprint and origin assumptions

### Checkpoint 2 — holes and slot
- add primary subtractive features
- render `checkpoint-2-features.png`
- export `checkpoint-2-features.step`
- summarize hole spacing, slot dimensions, and any clearance tradeoffs

### Checkpoint 3 — support block / refinement
- add the raised support or secondary bodies
- render `checkpoint-3-support.png`
- export `checkpoint-3-support.step`
- summarize massing and manufacturability implications

### Final handoff
- export `final.step`
- export `final.stl` if needed
- provide a compact parameter table
- explain which dimensions are safest to tweak later

## Chat-friendly reporting pattern

Use a short structure like:

```md
Checkpoint 2 complete.

Changed:
- Added two through-holes at ±25 mm
- Added centered through-slot, 24 x 8 mm

Artifacts:
- artifacts/checkpoint-2-features.png
- artifacts/checkpoint-2-features.step

Editable next:
- hole spacing
- hole radius
- slot length
- slot width
```

## Recommendation

If a human is reviewing asynchronously, send the PNG first and keep the STEP attached as the engineering artifact.
If a human is reviewing live, pair the PNG with an interactive viewer or a FreeCAD checkpoint opened from STEP.
