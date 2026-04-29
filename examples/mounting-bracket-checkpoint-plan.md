# Example: mounting bracket checkpoint plan

This example shows how an agent should structure a human-in-the-loop CAD session for a simple parametric mounting bracket.

## Requested part

- base plate
- two bolt holes
- centered slot
- raised support block

## Suggested workflow

### Checkpoint 1 — base plate only
Deliver:
- PNG preview of the base plate
- dimensions table
- note about coordinate origin and symmetry assumptions

Question to human:
- "Is the overall footprint correct before I add the mounting features?"

### Checkpoint 2 — holes and slot
Deliver:
- updated PNG preview
- STEP export
- parameters for hole spacing, hole radius, slot length, slot width

Question to human:
- "Do the mounting features look balanced, or should I move the holes or shorten the slot?"

### Checkpoint 3 — support block
Deliver:
- updated PNG preview
- STEP export
- support dimensions table

Question to human:
- "Should the support stay full width on the Y axis, or do you want it narrowed to save material?"

### Checkpoint 4 — final handoff
Deliver:
- final script
- STEP
- STL
- concise parameter table
- list of safest dimensions to tweak later

Question to human:
- "Do you want this optimized next for printability, machining, or appearance?"
