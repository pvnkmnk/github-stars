#!/usr/bin/env python3
"""
Category keyword loader for the star refresh pipeline.

Loads ``stars/categories.json`` and exposes the data in the tuple format
that ``update_stars.py`` already consumes via ``CATEGORY_KEYWORDS``.

A 4-tuple variant (emoji, name, strong, weak) preserves full backward
compatibility with the existing scoring code.  A 5-tuple variant
(emoji, name, strong, weak, phrases) is also available for when
multi-token phrase matching is wired into ``score_repo_for_category``.

Usage (one-line change in update_stars.py)::

    # before
    CATEGORY_KEYWORDS = [ ... 800 lines ... ]

    # after
    from categories import CATEGORY_KEYWORDS

If ``categories.json`` is missing or corrupt the module falls back to
a minimal built-in default so the pipeline never hard-crashes.
"""

from __future__ import annotations

import json
import logging
from pathlib import Path
from typing import Dict, List, Tuple

log = logging.getLogger("categories")

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parent.parent
STARS_DIR = PROJECT_ROOT / "stars"
CATEGORIES_JSON = STARS_DIR / "categories.json"

# ---------------------------------------------------------------------------
# Type aliases
# ---------------------------------------------------------------------------
# Backward-compatible format consumed by the existing score_repo_for_category
CategoryTuple4 = Tuple[str, str, List[str], List[str]]
# Extended format that also carries multi-token phrases
CategoryTuple5 = Tuple[str, str, List[str], List[str], List[str]]

# ---------------------------------------------------------------------------
# Fallback defaults (used only if categories.json is missing/corrupt)
# ---------------------------------------------------------------------------
_DEFAULT_CATEGORIES: List[Dict[str, List[str] | str]] = [
    {
        "emoji": "\U0001f4e1",  # 📡
        "name": "Homelab Infrastructure",
        "strong": ["self-host", "homelab", "selfhost", "reverse-proxy",
                     "wireguard", "tailscale", "proxmox", "docker"],
        "weak": ["server", "vpn", "proxy", "network", "dashboard"],
        "phrases": ["home server", "reverse proxy", "smart home"],
    },
    {
        "emoji": "\U0001f916",  # 🤖
        "name": "Agentic Dev Tools",
        "strong": ["agentic", "coding-agent", "AI-agent", "claude-code",
                     "aider", "copilot", "MCP-server"],
        "weak": ["agent", "coding", "LLM", "AI", "Claude"],
        "phrases": ["code assistant", "dev agent"],
    },
]

# ---------------------------------------------------------------------------
# Loader
# ---------------------------------------------------------------------------

def _load_raw() -> List[Dict[str, object]]:
    """Read and parse the JSON config, falling back to defaults on error."""
    try:
        with open(CATEGORIES_JSON, "r", encoding="utf-8") as fh:
            data = json.load(fh)
        cats = data.get("categories", [])
        if not cats:
            log.warning("categories.json contains no categories; using defaults")
            return _DEFAULT_CATEGORIES  # type: ignore[return-value]
        return cats  # type: ignore[return-value]
    except FileNotFoundError:
        log.warning("categories.json not found at %s; using built-in defaults",
                    CATEGORIES_JSON)
    except json.JSONDecodeError as exc:
        log.warning("categories.json is invalid JSON (%s); using built-in defaults",
                    exc)
    return _DEFAULT_CATEGORIES  # type: ignore[return-value]


def _validate(cat: Dict[str, object]) -> bool:
    """Return True if *cat* has the required keys with list values."""
    required = ("emoji", "name", "strong", "weak", "phrases")
    for key in required:
        if key not in cat:
            log.warning("Category missing key %r: %r", key, cat.get("name", "?"))
            return False
        val = cat[key]
        if key in ("strong", "weak", "phrases") and not isinstance(val, list):
            log.warning("Category %r key %r is not a list", cat.get("name", "?"), key)
            return False
        if key in ("emoji", "name") and not isinstance(val, str):
            log.warning("Category key %r is not a string", key)
            return False
    return True


def load_categories() -> List[Dict[str, object]]:
    """Load and validate the full category dicts from JSON.

    Returns a list of dicts, each with keys:
        emoji, name, strong, weak, phrases
    """
    raw = _load_raw()
    valid = [c for c in raw if _validate(c)]
    if not valid:
        log.warning("No valid categories found; using built-in defaults")
        return _DEFAULT_CATEGORIES  # type: ignore[return-value]
    if len(valid) < len(raw):
        log.warning("%d/%d categories passed validation",
                    len(valid), len(raw))
    return valid


# ---------------------------------------------------------------------------
# Tuple exports (consumed by update_stars.py)
# ---------------------------------------------------------------------------

def _to_4tuple(cat: Dict[str, object]) -> CategoryTuple4:
    """Convert a category dict to the legacy 4-tuple format."""
    return (
        str(cat["emoji"]),
        str(cat["name"]),
        list(cat["strong"]),  # type: ignore[arg-type]
        list(cat["weak"]),    # type: ignore[arg-type]
    )


def _to_5tuple(cat: Dict[str, object]) -> CategoryTuple5:
    """Convert a category dict to the extended 5-tuple format (with phrases)."""
    return (
        str(cat["emoji"]),
        str(cat["name"]),
        list(cat["strong"]),  # type: ignore[arg-type]
        list(cat["weak"]),    # type: ignore[arg-type]
        list(cat["phrases"]), # type: ignore[arg-type]
    )


# Eagerly loaded at import time so update_stars.py can do a simple
# ``from categories import CATEGORY_KEYWORDS`` one-liner.
_raw_categories: List[Dict[str, object]] = load_categories()

#: Backward-compatible 4-tuples — drop-in replacement for the hardcoded list.
CATEGORY_KEYWORDS: List[CategoryTuple4] = [
    _to_4tuple(c) for c in _raw_categories
]

#: Extended 5-tuples that also include multi-token phrases.
#: Use this when score_repo_for_category is updated to score phrases.
CATEGORY_KEYWORDS_WITH_PHRASES: List[CategoryTuple5] = [
    _to_5tuple(c) for c in _raw_categories
]

#: Full dicts for any code that needs direct access to all fields.
CATEGORY_DICTS: List[Dict[str, object]] = _raw_categories


def get_category_names() -> List[str]:
    """Return just the category names (handy for logging / argparse choices)."""
    return [c[1] for c in CATEGORY_KEYWORDS]


if __name__ == "__main__":
    # Quick sanity check when run directly
    print(f"Loaded {len(CATEGORY_KEYWORDS)} categories from {CATEGORIES_JSON}")
    for emoji, name, strong, weak, phrases in CATEGORY_KEYWORDS_WITH_PHRASES:
        print(f"  {emoji} {name}: {len(strong)} strong, "
              f"{len(weak)} weak, {len(phrases)} phrases")
