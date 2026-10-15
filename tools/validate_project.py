#!/usr/bin/env python3
"""Dependency-free static checks for the Ren'Py source tree."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
GAME = ROOT / "game"
LABEL_RE = re.compile(r"^\s*label\s+([A-Za-z_]\w*)\s*(?:\([^\n]*?\))?\s*:", re.M)
FLOW_RE = re.compile(r"^\s*(?:jump|call)\s+([A-Za-z_]\w*)\b", re.M)
SCREEN_JUMP_RE = re.compile(r"\bJump\(\s*['\"]([A-Za-z_]\w*)['\"]\s*\)")
AUDIO_RE = re.compile(r"\b(?:safe_play_sound|safe_play_music)\(\s*['\"]([^'\"]+)['\"]")


def validate() -> tuple[list[str], dict[str, int]]:
    errors: list[str] = []
    files = sorted(GAME.rglob("*.rpy")) if GAME.exists() else []
    if not files:
        return ["No .rpy source files found under game/"], {}

    labels: dict[str, Path] = {}
    duplicates: list[tuple[str, Path]] = []
    flow_targets: list[tuple[str, Path]] = []
    audio_targets: list[tuple[str, Path]] = []
    for path in files:
        source = path.read_text(encoding="utf-8-sig")
        for label in LABEL_RE.findall(source):
            if label in labels:
                duplicates.append((label, path))
            else:
                labels[label] = path
        flow_targets.extend((name, path) for name in FLOW_RE.findall(source))
        flow_targets.extend((name, path) for name in SCREEN_JUMP_RE.findall(source))
        audio_targets.extend((name, path) for name in AUDIO_RE.findall(source))

    for label, path in duplicates:
        errors.append(f"Duplicate label '{label}' in {path.relative_to(ROOT)}")
    for target, path in flow_targets:
        if target not in labels:
            errors.append(f"Unknown story target '{target}' in {path.relative_to(ROOT)}")
    for target, path in audio_targets:
        if not (GAME / target).is_file():
            errors.append(f"Missing audio asset '{target}' referenced in {path.relative_to(ROOT)}")

    chinese_font = GAME / "fonts" / "chinese.ttf"
    if not chinese_font.is_file() or chinese_font.stat().st_size < 1024:
        errors.append("Missing bundled Chinese display font: game/fonts/chinese.ttf")

    for image in sorted((GAME / "images").rglob("*.png")) if (GAME / "images").exists() else []:
        if image.stat().st_size == 0:
            errors.append(f"Empty image asset: {image.relative_to(ROOT)}")

    flags = (GAME / "00_project_flags.rpy").read_text(encoding="utf-8-sig")
    for flag, expected in (("DEV_MODE", "False"), ("DEMO_BUILD", "True"), ("AUTO_AUDIO_PLACEHOLDER", "False")):
        if not re.search(rf"\b{flag}\s*=\s*{expected}\b", flags):
            errors.append(f"Release default must be {flag} = {expected}")

    audio_helpers = (GAME / "04_audio_safe.rpy").read_text(encoding="utf-8-sig")
    if "renpy.sound.set_volume" in audio_helpers or "renpy.music.set_volume" in audio_helpers:
        errors.append("Audio helpers must not overwrite the player's mixer/channel volume preference")

    stats = {
        "script_files": len(files),
        "labels": len(labels),
        "story_references": len(flow_targets),
        "audio_references": len(audio_targets),
    }
    return errors, stats


def main() -> int:
    errors, stats = validate()
    if errors:
        print("Project validation failed:")
        for error in errors:
            print(f"  - {error}")
        return 1

    print("Project validation passed:")
    print(f"  {stats['script_files']} Ren'Py source files")
    print(f"  {stats['labels']} unique labels - {stats['story_references']} story references")
    print(f"  {stats['audio_references']} audio references resolve")
    print("  bundled font and visual assets are present")
    print("  release defaults and audio mixer behavior are safe")
    return 0


if __name__ == "__main__":
    sys.exit(main())
