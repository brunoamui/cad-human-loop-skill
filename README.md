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
skills/
  cad-human-loop/
    SKILL.md
references/
  workflow-blueprint.md
  checkpoint-template.md
examples/
  cadquery/
    mounting_bracket.py
  build123d/
    mounting_bracket.py
  mounting-bracket-checkpoint-plan.md
  artifact-workflow.md
scripts/
  generate_checkpoints.py
```

The repo now supports both:
- a **root skill file** for simple standalone use
- a **plugin-friendly `skills/cad-human-loop/SKILL.md` layout** for collections and plugin-style packaging

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

### As a plugin-friendly skill package
This repo also includes the canonical plugin-discoverable layout:

```text
skills/cad-human-loop/SKILL.md
```

and a minimal plugin entrypoint:

```text
index.js
package.json
```

That makes the repository usable both as a standalone skill repo and as a lightweight plugin-style package that exposes `./skills/*`.

## Who this is for

- people building CAD-capable coding agents
- teams doing review-heavy parametric design
- workflows where a human needs to approve geometry before final export

## Philosophy

The core idea is simple:

> keep the source of truth in code, keep the progress visible in images and STEP files, and keep the conversation about geometry rather than hidden agent state.

## Included runnable examples

The repo includes concrete example scripts for the same parametric mounting bracket in both major script-first CAD styles:

- `examples/build123d/mounting_bracket.py`
- `examples/cadquery/mounting_bracket.py`

It also includes an artifact-oriented workflow note:

- `examples/artifact-workflow.md`

and a real helper script for checkpoint generation:

- `scripts/generate_checkpoints.py`

Those examples are intentionally structured to make checkpointing easy: dimensions are exposed up top, the part construction is broken into understandable phases, and export calls are included as commented examples.

## Generate checkpoint artifacts

If you have the relevant CAD library installed, you can generate real checkpoint artifacts from the included examples.

### build123d

```bash
python scripts/generate_checkpoints.py --module build123d --output-dir artifacts/build123d --stl
```

### CadQuery

```bash
python scripts/generate_checkpoints.py --module cadquery --output-dir artifacts/cadquery --stl
```

The helper writes:
- checkpoint STEP files
- optional checkpoint STL files
- `parameters.json`
- `parameters.md`
- PNG screenshots when `ocp_vscode` is installed and screenshot capture is available

## License

MIT
