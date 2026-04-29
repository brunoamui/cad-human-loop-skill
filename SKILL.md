---
name: cad-human-loop
description: Human-in-the-loop CAD workflow for coding agents. Use for parametric part design where agents should show visible progress, pause at clear checkpoints, discuss tradeoffs in plain language, and hand off reviewable artifacts such as PNG previews, STEP files, and parameter tables. Prefers build123d or CadQuery for authoring, with FreeCAD as a review or intervention surface when needed.
---

# CAD Human Loop

## Default posture
Prefer script-first parametric CAD.
Default to build123d or CadQuery for authoring.
Use FreeCAD mainly as a review, inspection, or manual intervention surface.
Keep the human in the loop with explicit visual checkpoints rather than silent long-running generation.

## What this skill is for
Use this skill when a coding agent must design or refine 3D CAD objects and the human should be able to:
- see progress while the part is evolving
- discuss changes in plain language
- approve or redirect the design at clear checkpoints
- inspect artifacts in common tools like FreeCAD or browser viewers

This skill is for engineering-style CAD workflows, not artistic text-to-mesh generation.

## Tool selection

### Preferred authoring tools
1. **build123d** — best default for maintainable, reviewable agent-generated CAD code
2. **CadQuery** — great when faster script generation matters more than explicitness
3. **FreeCAD scripting / MCP** — use when native FreeCAD documents, GUI co-piloting, or PartDesign-specific review matters

### Why this order
- build123d is easier to review and repair because the modeling flow is explicit
- CadQuery is shorter and often faster to generate, but fluent chains are denser and easier to mis-sequence
- FreeCAD is strongest as a human-facing review surface, not as the primary authoring substrate for LLMs

## Core rule: visible checkpoints over hidden work
The agent should not disappear for a long stretch and return only with a final STEP or STL.

Instead, the agent should work in small visible phases. After each phase, produce:
1. a short natural-language summary of what changed
2. one visual artifact
3. one machine-usable artifact
4. the key editable parameters for that phase

### Minimum checkpoint bundle
- **summary**: one or two sentences
- **preview**: PNG screenshot or interactive viewer state
- **artifact**: STEP preferred, STL optional, SVG for 2D review if useful
- **parameters**: dimensions or feature settings changed in the step

## Default human-in-the-loop workflow

### Recommended workflow
**Agent authors in build123d or CadQuery**
→ **shows progress through OCP Viewer or screenshot checkpoints**
→ **exports STEP at every major checkpoint**
→ **human reviews in chat, browser viewer, or FreeCAD**
→ **agent maps feedback back to code and parameters**

### Why this is the default
It keeps the source of truth in code, which is easier for the agent to regenerate, diff, test, and explain.
It also gives the human concrete visuals and portable CAD artifacts instead of opaque internal state.

## Workflow variants

### Variant A — best overall
Use when the human is comfortable with a code-first workflow.

**Stack**:
- build123d or CadQuery
- OCP Viewer / ocp_vscode or notebook viewer
- PNG screenshots at checkpoints
- STEP export at checkpoints

**Loop**:
1. Agent creates or updates the parametric script.
2. Agent renders a checkpoint preview.
3. Agent explains what changed and what is still uncertain.
4. Human gives feedback in plain language.
5. Agent edits parameters or geometry code and repeats.

### Variant B — review in FreeCAD
Use when the human wants to inspect geometry in a familiar CAD tool.

**Stack**:
- build123d or CadQuery for authoring
- STEP export after each checkpoint
- FreeCAD for inspection and comments

**Loop**:
1. Agent exports `checkpoint-N.step`.
2. Human opens it in FreeCAD.
3. Human comments on proportions, placements, clearances, or manufacturability.
4. Agent updates the script instead of editing the STEP directly.

### Variant C — live FreeCAD co-pilot
Use when the human wants a shared GUI cockpit and is comfortable steering with selection and viewport context.

**Stack**:
- FreeCAD with MCP bridge or AI workbench
- screenshot / selection tools
- optional plan mode before execution

**Loop**:
1. Agent proposes the next operation.
2. Human approves or redirects.
3. Agent executes one operation or one small group.
4. Agent captures screenshot and explains the effect.

Use this only when GUI co-steering matters more than authoring reliability.

## Phase structure the agent should follow

### Phase 0 — clarify intent
Before generating geometry, the agent should restate:
- the object being designed
- the functional constraints
- the dimensions already known
- the open questions or assumptions

If ambiguity is high, the agent should ask for clarification before geometry creation.
If ambiguity is low, the agent should state assumptions and continue.

### Phase 1 — base shape
Create the primary massing or base body.

Checkpoint deliverables:
- preview of base shape
- dimensions table for the base
- one-sentence explanation of coordinate system and origin assumptions

### Phase 2 — primary features
Add holes, cutouts, slots, bosses, support blocks, or other defining features.

Checkpoint deliverables:
- updated preview
- list of added features and their dimensions
- any detected risk around feature placement, clearance, or wall thickness

### Phase 3 — refinement
Add fillets, chamfers, patterns, symmetry cleanup, or manufacturing tweaks.

Checkpoint deliverables:
- before/after summary
- updated preview
- note if any downstream manufacturing behavior changes

### Phase 4 — handoff
Export final artifacts and summarize how to change the model later.

Required deliverables:
- final script
- STEP
- STL if useful
- parameter table
- short explanation of which parameters are safe to adjust

## How the agent should talk to the human
The agent should use plain language tied to visible geometry.

Good:
- "I added the two mounting holes at ±25 mm from center. The support block is now sitting on the top face rather than intersecting the base plane."
- "This slot is centered and cut through the full thickness. If you want more material around it, I can shorten it or move the bolt holes outward."

Avoid:
- unexplained CAD API jargon
- only describing code instead of the resulting geometry
- saying work is done without showing a preview or artifact

## Checkpoint template
Use this structure at every meaningful milestone:

```md
### Checkpoint N — <name>

What changed:
- ...

Visible result:
- <png path or viewer name>

Artifacts:
- <step path>
- <stl path if any>

Editable parameters:
- width = ...
- height = ...
- hole_spacing = ...

Notes / risks:
- ...

Suggested next decision for the human:
- approve / adjust / compare option A vs B
```

## Artifact priorities

### Best for discussion
1. **PNG screenshots** — easiest to paste into chat and react to quickly
2. **interactive OCP viewer state** — best for live review
3. **STEP** — best neutral handoff format for CAD inspection
4. **SVG projections** — useful when 2D technical review matters

### Weak primary artifacts
- STL alone — okay for printing, weak for engineering review
- FCStd alone — strong inside FreeCAD, weak for portable discussion
- raw code alone — not enough for non-technical reviewers

## Review surface guidance

### OCP Viewer / ocp_vscode
Best general-purpose review surface for build123d and CadQuery.
Use it for live iteration and named intermediate objects.

### PNG screenshot sequence
Best for async review and chat-based discussion.
The agent should save one screenshot per major checkpoint and name them clearly.

### FreeCAD
Best when the human wants full CAD inspection, direct orbiting, measurements, or manual edits.
Prefer opening exported STEP files unless the workflow truly needs native FreeCAD document state.

## Parameter discipline
The agent should expose human-editable dimensions near the top of the script and keep names obvious.

Good examples:
- `BASE_LENGTH`
- `SUPPORT_HEIGHT`
- `BOLT_HOLE_SPACING`
- `SLOT_WIDTH`

Avoid hiding key dimensions deep inside modeling calls.

## Validation rules
At each major checkpoint, validate at least:
- model builds without errors
- expected key dimensions match the request
- exported STEP succeeds
- exported STL succeeds if requested
- screenshots or previews actually reflect the current model

If the agent can measure geometry programmatically, report:
- bounding box
- volume
- center or symmetry assumptions

## Human-in-the-middle policies

### When to pause automatically
Pause for human review when:
- the base form is created
- a visible interpretation choice was made
- a dimension had to be assumed
- a manufacturability tradeoff appears
- the final handoff is ready

### When not to pause
Do not pause for every trivial internal refactor or tiny code cleanup unless it changes visible geometry or a functional constraint.

## FreeCAD-specific guidance
If using FreeCAD in the loop:
- prefer screenshot and selection-aware workflows over large opaque macro dumps
- keep changes small and explain each feature operation in natural language
- export STEP at checkpoints so the design is reviewable outside the live session
- if the human starts editing manually in FreeCAD, treat FreeCAD as the new source of truth until the script is synchronized again

## What to deliver at the end
The final answer should include:
1. what was designed and why
2. the main parameters
3. the final files produced
4. what the human can change safely next
5. any unresolved design risks or open decisions

## Anti-patterns
Avoid these:
- generating a final part with no intermediate previews
- using FreeCAD GUI automation as the default path for simple parametric parts
- hiding assumptions instead of stating them
- only returning STL when a STEP review loop is feasible
- discussing code structure without relating it back to visible geometry
- changing several design choices between checkpoints without calling them out

## Quick recommendation table

| Need | Best choice |
|---|---|
| Most maintainable agent-authored CAD | build123d |
| Fastest script generation | CadQuery |
| Human wants a familiar CAD inspection tool | STEP + FreeCAD |
| Human wants live shared GUI steering | FreeCAD MCP / AI workbench |
| Async feedback in chat | PNG checkpoints + parameter table |

## Use this sentence when kicking off the workflow
"I’m going to model this in a script-first CAD workflow, show visible checkpoints as the shape evolves, and pause at the main design decisions so you can steer without losing momentum."
