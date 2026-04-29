#!/usr/bin/env python3
"""Generate human-in-the-loop CAD checkpoint artifacts.

This script loads one of the example CAD modules, builds named checkpoints,
and writes reviewable artifacts into an output directory.

Outputs:
- `<checkpoint>.step` for every checkpoint
- `<checkpoint>.stl` optionally
- `parameters.json`
- `parameters.md`
- PNG screenshots when `ocp_vscode` is installed and screenshot capture works
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from pathlib import Path
from typing import Any


def load_module(module_path: Path):
    spec = importlib.util.spec_from_file_location(module_path.stem, module_path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Could not load module from {module_path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def write_parameters(output_dir: Path, parameters: dict[str, Any]) -> None:
    (output_dir / "parameters.json").write_text(
        json.dumps(parameters, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )

    lines = ["# Parameters", "", "| Name | Value |", "|---|---:|"]
    for key, value in sorted(parameters.items()):
        lines.append(f"| `{key}` | `{value}` |")
    (output_dir / "parameters.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def try_save_screenshot(name: str, obj: Any, output_path: Path) -> bool:
    try:
        from ocp_vscode import save_screenshot, show

        show(obj, name=name)
        save_screenshot(str(output_path))
        return True
    except Exception:
        return False


def export_build123d(checkpoints: dict[str, Any], output_dir: Path, export_stl: bool) -> None:
    from build123d import export_step, export_stl

    for name, part in checkpoints.items():
        export_step(part, str(output_dir / f"{name}.step"))
        if export_stl:
            export_stl(part, str(output_dir / f"{name}.stl"))
        try_save_screenshot(name, part, output_dir / f"{name}.png")


def export_cadquery(checkpoints: dict[str, Any], output_dir: Path, export_stl: bool) -> None:
    from cadquery import exporters

    for name, part in checkpoints.items():
        exporters.export(part, str(output_dir / f"{name}.step"))
        if export_stl:
            exporters.export(part, str(output_dir / f"{name}.stl"))
        try_save_screenshot(name, part, output_dir / f"{name}.png")


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate CAD checkpoint artifacts")
    parser.add_argument(
        "--module",
        required=True,
        choices=["build123d", "cadquery"],
        help="Which example module to run",
    )
    parser.add_argument(
        "--output-dir",
        default="artifacts",
        help="Directory where artifacts will be written",
    )
    parser.add_argument(
        "--stl",
        action="store_true",
        help="Also export STL files for each checkpoint",
    )
    args = parser.parse_args()

    repo_root = Path(__file__).resolve().parent.parent
    module_path = repo_root / "examples" / args.module / "mounting_bracket.py"
    output_dir = Path(args.output_dir).resolve()
    output_dir.mkdir(parents=True, exist_ok=True)

    module = load_module(module_path)

    if not hasattr(module, "build_checkpoint_parts"):
        raise RuntimeError(f"Module {module_path} does not define build_checkpoint_parts()")

    checkpoints = module.build_checkpoint_parts()
    parameters = getattr(module, "PARAMETERS", {})
    write_parameters(output_dir, parameters)

    if args.module == "build123d":
        export_build123d(checkpoints, output_dir, args.stl)
    else:
        export_cadquery(checkpoints, output_dir, args.stl)

    print(f"Wrote checkpoint artifacts to {output_dir}")
    for checkpoint_name in checkpoints:
        print(f"- {checkpoint_name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
