#!/usr/bin/env python3
"""Apply workshop checkpoints while archiving replaced files."""

import argparse
import json
import shutil
from datetime import datetime
from pathlib import Path
from typing import List, Optional


SKILL_ROOT = Path(__file__).resolve().parents[1]
REPO_ROOT = Path(__file__).resolve().parents[4]
CHECKPOINT_ROOT = SKILL_ROOT / "assets" / "checkpoints"
MANIFEST_PATH = CHECKPOINT_ROOT / "manifest.json"
ARCHIVE_ROOT = REPO_ROOT / ".workshop_archives"

PROTECTED_PARTS = {".codex", ".git", ".workshop_archives", "results"}


def load_manifest() -> dict:
    return json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))


def normalize_name(name: str, manifest: dict) -> str:
    key = name.strip().lower().replace("_", "-")
    checkpoints = manifest["checkpoints"]
    aliases = manifest["aliases"]
    if key in checkpoints:
        return key
    if key in aliases:
        return aliases[key]
    available = sorted(set(checkpoints) | set(aliases))
    raise SystemExit(
        "Unknown checkpoint '{}'. Available names: {}".format(
            name, ", ".join(available)
        )
    )


def checkpoint_files(checkpoint: str) -> List[Path]:
    root = CHECKPOINT_ROOT / checkpoint
    if not root.is_dir():
        raise SystemExit("Checkpoint assets not found: {}".format(root))
    files = [path for path in root.rglob("*") if path.is_file()]
    return sorted(files, key=lambda path: path.relative_to(root).as_posix())


def ensure_safe_relative_path(rel_path: Path) -> None:
    if rel_path.is_absolute() or ".." in rel_path.parts:
        raise SystemExit("Unsafe checkpoint path: {}".format(rel_path))
    if rel_path.parts and rel_path.parts[0] in PROTECTED_PARTS:
        raise SystemExit("Refusing to overwrite protected path: {}".format(rel_path))


def make_archive_dir(checkpoint: str) -> Path:
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    base = ARCHIVE_ROOT / "{}_{}".format(timestamp, checkpoint)
    archive_dir = base
    suffix = 1
    while archive_dir.exists():
        suffix += 1
        archive_dir = Path("{}_{}".format(base, suffix))
    archive_dir.mkdir(parents=True)
    return archive_dir


def apply_checkpoint(checkpoint: str, dry_run: bool = False) -> Optional[Path]:
    source_root = CHECKPOINT_ROOT / checkpoint
    files = checkpoint_files(checkpoint)
    rel_paths = [path.relative_to(source_root) for path in files]
    for rel_path in rel_paths:
        ensure_safe_relative_path(rel_path)

    print("Checkpoint: {}".format(checkpoint))
    print("Files to replace:")
    for rel_path in rel_paths:
        target = REPO_ROOT / rel_path
        marker = "exists" if target.exists() else "new"
        print("  {} ({})".format(rel_path.as_posix(), marker))

    if dry_run:
        print("Dry run only; no files changed.")
        return None

    archive_dir = make_archive_dir(checkpoint)
    missing = []  # type: List[str]

    for src_path, rel_path in zip(files, rel_paths):
        target = REPO_ROOT / rel_path
        archive_target = archive_dir / rel_path
        if target.exists():
            archive_target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(str(target), str(archive_target))
        else:
            missing.append(rel_path.as_posix())

        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(str(src_path), str(target))

    if missing:
        (archive_dir / "_missing_before_checkpoint.txt").write_text(
            "\n".join(missing) + "\n", encoding="utf-8"
        )

    print("Applied checkpoint {}.".format(checkpoint))
    print("Archived replaced files in: {}".format(archive_dir))
    return archive_dir


def list_checkpoints(manifest: dict) -> None:
    for name, details in manifest["checkpoints"].items():
        print("{}: {} - {}".format(name, details["title"], details["description"]))


def status(manifest: dict) -> None:
    matches = []  # type: List[str]
    for checkpoint in manifest["checkpoints"]:
        source_root = CHECKPOINT_ROOT / checkpoint
        files = checkpoint_files(checkpoint)
        if all(
            (REPO_ROOT / path.relative_to(source_root)).is_file()
            and (REPO_ROOT / path.relative_to(source_root)).read_bytes()
            == path.read_bytes()
            for path in files
        ):
            matches.append(checkpoint)

    if matches:
        print("Current files match checkpoint asset contents for:")
        for checkpoint in matches:
            print("  {}".format(checkpoint))
    else:
        print("Current files do not exactly match any checkpoint asset set.")


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Manage AI Code Assistants workshop checkpoints."
    )
    subparsers = parser.add_subparsers(dest="command")

    subparsers.add_parser("list", help="List available checkpoints.")
    subparsers.add_parser("status", help="Check which checkpoint files match.")

    apply_parser = subparsers.add_parser(
        "apply", help="Apply a checkpoint after archiving replaced files."
    )
    apply_parser.add_argument("checkpoint", help="Checkpoint name or alias.")
    apply_parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show files that would be replaced without changing them.",
    )

    args = parser.parse_args()
    if not args.command:
        parser.print_help()
        return 2

    manifest = load_manifest()

    if args.command == "list":
        list_checkpoints(manifest)
        return 0
    if args.command == "status":
        status(manifest)
        return 0
    if args.command == "apply":
        checkpoint = normalize_name(args.checkpoint, manifest)
        apply_checkpoint(checkpoint, dry_run=args.dry_run)
        return 0

    raise SystemExit("Unhandled command: {}".format(args.command))


if __name__ == "__main__":
    raise SystemExit(main())
