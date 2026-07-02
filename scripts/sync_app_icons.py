#!/usr/bin/env python3
"""Sync App Store artwork URLs from the iTunes Lookup API into _data/app_icons.yml."""

from __future__ import annotations

import json
import re
import time
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
APPS_PATH = ROOT / "_data" / "apps.yml"
ICONS_PATH = ROOT / "_data" / "app_icons.yml"
LOOKUP = "https://itunes.apple.com/us/lookup"


def parse_apps(text: str) -> list[tuple[str, str | None]]:
    blocks = re.split(r"(?:^|\n)- id: ", text)
    apps: list[tuple[str, str | None]] = []
    for block in blocks:
        if not block.strip():
            continue
        app_id = block.split("\n", 1)[0].strip()
        match = re.search(r"apple_id:\s*(\d+)", block)
        apps.append((app_id, match.group(1) if match else None))
    return apps


def fetch_artwork(apple_id: str) -> dict[str, str] | None:
    url = f"{LOOKUP}?id={apple_id}&entity=software"
    with urllib.request.urlopen(url, timeout=20) as resp:
        data = json.load(resp)
    if not data.get("resultCount"):
        return None
    item = data["results"][0]
    return {
        "icon_url": item.get("artworkUrl512", ""),
        "icon_url_sm": item.get("artworkUrl100", ""),
    }


def main() -> None:
    apps = parse_apps(APPS_PATH.read_text(encoding="utf-8"))
    lines = [
        "# App Store artwork URLs synced from the iTunes Lookup API.",
        "# Regenerate: python3 scripts/sync_app_icons.py",
        "",
    ]
    updated = 0
    skipped = 0

    for app_id, apple_id in apps:
        if not apple_id:
            print(f"skip {app_id}: no apple_id")
            skipped += 1
            continue
        print(f"sync {app_id} ({apple_id})… ", end="", flush=True)
        artwork = fetch_artwork(apple_id)
        if not artwork or not artwork["icon_url"]:
            print("no artwork")
            skipped += 1
            continue
        print("ok")
        lines.extend(
            [
                f"{app_id}:",
                f'  icon_url: "{artwork["icon_url"]}"',
                f'  icon_url_sm: "{artwork["icon_url_sm"]}"',
                "",
            ]
        )
        updated += 1
        time.sleep(0.15)

    ICONS_PATH.write_text("\n".join(lines), encoding="utf-8")
    print(f"\nDone: {updated} updated, {skipped} skipped → {ICONS_PATH}")


if __name__ == "__main__":
    main()
