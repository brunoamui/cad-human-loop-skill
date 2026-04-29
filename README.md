# cad-human-loop

An open OpenCode skill for **human-in-the-loop CAD with coding agents**.

It is designed for workflows where an agent should not silently generate a final 3D model, but instead:

- design parts in **build123d** or **CadQuery**
- show **visible progress** through screenshots or interactive previews
- pause at clear checkpoints for human feedback
- hand off **STEP/STL and parameter tables** cleanly
- use **FreeCAD as a review/intervention surface** when needed

## What this skill teaches

The skill gives agents a practical workflow for:

- script-first parametric CAD
- progress reporting with checkpoint artifacts
- easy discussion with humans in the middle of the loop
- choosing between build123d, CadQuery, and FreeCAD
- exporting artifacts that are actually reviewable

## Recommended default stack

**build123d or CadQuery for authoring**  
**+ OCP Viewer or screenshots for progress**  
**+ STEP export at checkpoints**  
**+ FreeCAD for optional inspection or intervention**

## Repository layout

```text
SKILL.md
references/
  workflow-blueprint.md
  checkpoint-template.md
examples/
  mounting-bracket-checkpoint-plan.md
```

## Install

### As a local OpenCode skill
Copy or symlink the skill directory into your OpenCode skills folder.
The local directory name should be `cad-human-loop` to match the skill frontmatter name.

Example:

```bash
mkdir -p ~/.config/opencode/skills
ln -s /path/to/cad-human-loop-skill ~/.config/opencode/skills/cad-human-loop
```

Or copy just the root skill file and companion folders if your setup expects that layout.

## Who this is for

- people building CAD-capable coding agents
- teams doing review-heavy parametric design
- workflows where a human needs to approve geometry before final export

## Philosophy

The core idea is simple:

> keep the source of truth in code, keep the progress visible in images and STEP files, and keep the conversation about geometry rather than hidden agent state.

## License

MIT
