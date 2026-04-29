# Checkpoint template

Use this template when reporting design progress to a human reviewer.

```md
## Checkpoint <N> — <name>

### What changed
- ...

### Why it changed
- ...

### Preview
- PNG: `artifacts/checkpoint-<N>.png`
- Viewer: `<viewer name or session>`

### Artifacts
- STEP: `artifacts/checkpoint-<N>.step`
- STL: `artifacts/checkpoint-<N>.stl`

### Parameters changed
- BASE_LENGTH = ...
- SLOT_WIDTH = ...
- HOLE_SPACING = ...

### Risks / assumptions
- ...

### Best next decision for the human
- approve
- adjust dimensions
- compare options
```

## Notes

- Prefer plain language over API jargon.
- Describe visible geometry, not just code edits.
- If a choice is ambiguous, show two options before locking in the next phase.
