# Workflow blueprint

## Default architecture

```text
Human request
  -> Agent clarifies constraints
  -> Agent writes parametric CAD script
  -> Agent generates checkpoint preview
  -> Human reviews visible result
  -> Agent revises parameters or geometry
  -> Agent exports STEP/STL
  -> Human approves or asks for another pass
```

## Best default tool split

- **Authoring**: build123d first, CadQuery second
- **Live preview**: OCP Viewer / ocp_vscode
- **Async preview**: PNG screenshots
- **Neutral CAD handoff**: STEP
- **Review GUI**: FreeCAD

## Decision guide

### Choose build123d when
- long-lived maintainability matters
- another human or agent will review the code
- the workflow benefits from explicit sketch/extrude style structure

### Choose CadQuery when
- the part is straightforward
- fast iteration matters more than explicit structure
- fluent workplane chaining is acceptable

### Choose FreeCAD-centered flow when
- the human wants a live CAD GUI
- native FreeCAD documents matter
- the review loop depends on selections, screenshots, or direct GUI intervention

## Mandatory checkpoints

1. **Base shape checkpoint**
2. **Primary feature checkpoint**
3. **Refinement checkpoint**
4. **Final handoff checkpoint**

## Minimal deliverables at each checkpoint

- one PNG or interactive preview
- one short explanation of what changed
- one exported STEP if geometry materially changed
- one list of editable parameters

## Human feedback prompts

Use prompts like:

- "Does the overall proportion feel right before I add holes and cutouts?"
- "Do you want the slot centered, shortened, or moved before I continue?"
- "I can trade wall thickness for clearance here — which matters more?"
- "Should I optimize this for easier printing, easier machining, or a cleaner shape?"
