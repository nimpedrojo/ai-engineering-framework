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


def main() -> None:
    framework_root = Path(__file__).resolve().parents[1]
    target_root = Path.cwd()

    templates = framework_root / "templates"
    scripts = framework_root / "scripts"

    if not templates.exists():
        fail("templates folder not found")

    files = [
        (templates / "AGENTS.md", target_root / "AGENTS.md"),
        (
            templates / ".github" / "copilot-instructions.md",
            target_root / ".github" / "copilot-instructions.md",
        ),
        (
            templates / "prompts" / "discovery.md",
            target_root / "docs" / "ai" / "prompts" / "discovery.md",
        ),
        (
            scripts / "aif-finish",
            target_root / "scripts" / "aif-finish",
        ),
    ]

    print()
    print("AI Engineering Framework Init")
    print("-----------------------------")
    print()

    for source, target in files:
        if not source.exists():
            fail(f"missing source file: {source}")

        if target.exists():
            print(f"• Skipped existing file: {target}")
            continue

        copy_file(source, target)

    print()
    print("Framework installed.")
    print()
    print("Next step:")
    print("1. Open docs/ai/prompts/discovery.md")
    print("2. Use it with Codex to start project discovery")
    print()


if __name__ == "__main__":
    main()