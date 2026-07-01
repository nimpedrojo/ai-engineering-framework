#!/usr/bin/env python3

from pathlib import Path
import shutil
import sys


def fail(message: str) -> None:
    print(f"ERROR: {message}")
    sys.exit(1)


def copy_file(source: Path, target: Path) -> None:
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, target)
    print(f"✔ {target}")


def copy_dir(source: Path, target: Path) -> None:
    if target.exists():
        print(f"• Skipped existing folder: {target}")
        return

    shutil.copytree(source, target)
    print(f"✔ {target}")


def main() -> None:
    framework_root = Path(__file__).resolve().parents[1]
    target_root = Path.cwd()

    templates = framework_root / "templates"
    scripts = framework_root / "scripts"

    if not templates.exists():
        fail("templates folder not found")

    print()
    print("AI Migration Harness Init")
    print("-------------------------")
    print()

    copy_file(templates / "AGENTS.md", target_root / "AGENTS.md")
    copy_dir(templates / ".github", target_root / ".github")
    copy_dir(templates / "docs" / "ai-harness", target_root / "docs" / "ai-harness")
    copy_dir(templates / "prompts", target_root / "prompts")
    copy_file(scripts / "aif-finish", target_root / "scripts" / "aif-finish")

    print()
    print("Harness installed.")
    print()
    print("Next step:")
    print("1. Open docs/ai-harness/README.md")
    print("2. Start with prompts/discovery.md")
    print()
    

if __name__ == "__main__":
    main()