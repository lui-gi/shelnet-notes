#!/usr/bin/env python3
"""
Syncs notes.json with the contents of the notes/ directory.
Run this after adding, renaming, or removing notes.
"""

import json
from pathlib import Path

NOTES_DIR = Path(__file__).parent / "notes"
INDEX_FILE = Path(__file__).parent / "notes.json"


def sync_notes():
    # Get all .md files, excluding README
    notes = [
        {"path": f"notes/{f.name}"}
        for f in NOTES_DIR.glob("*.md")
        if "readme" not in f.name.lower()
    ]

    # Sort by filename descending (newest date first)
    notes.sort(key=lambda x: x["path"], reverse=True)

    # Write to notes.json
    with open(INDEX_FILE, "w", encoding="utf-8") as f:
        json.dump(notes, f, indent=2)

    print(f"Synced {len(notes)} notes to notes.json")
    for note in notes:
        print(f"  - {note['path']}")


if __name__ == "__main__":
    sync_notes()
