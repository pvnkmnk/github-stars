"""Shared fixtures for the scoring pipeline test suite."""
import sys
from pathlib import Path

import pytest

# Ensure the scripts directory is on sys.path for imports
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))


# ── Sample repos for scoring tests ──────────────────────────────

@pytest.fixture
def sample_repos():
    """Collection of sample repos exercising different scoring features."""
    return [
        # (stars, full_name, language, description)
        # Phrase match: "reverse proxy" in description
        (500, "nginx/proxy-manager", "Go",
         "A reverse proxy and nginx proxy manager for home server"),
        # Star bonus: 185k stars → +5 (capped)
        (185_000, "microsoft/vscode", "TypeScript",
         "Visual Studio Code - code editor for debugging web apps"),
        # Expanded keyword: "copilot" was missing before
        (12_000, "github/copilot-cli", "TypeScript",
         "GitHub Copilot CLI - your AI pair programmer for the terminal"),
        # Phrase match: "machine learning"
        (8_000, "pytorch/pytorch", "C++",
         "Tensors and neural networks with GPU acceleration for machine learning"),
        # Expanded keyword: "authentik"
        (3_500, "goauthentik/authentik", "Python",
         "The authentication glue for your homelab"),
        # Edge case: empty description
        (100, "user/empty-repo", "Python", ""),
    ]


@pytest.fixture
def sample_repo_with_phrases():
    """A repo whose description contains known multi-token phrases."""
    return (
        10_000, "myuser/homelab-tool", "Python",
        "A reverse proxy and home server manager with machine learning support"
    )


# ── Keyword fixtures ────────────────────────────────────────────

@pytest.fixture
def homelab_keywords():
    """Minimal Homelab Infrastructure keywords for isolated tests."""
    strong = ["self-host", "homelab", "reverse-proxy", "tailscale"]
    weak = ["server", "proxy", "dashboard", "network"]
    phrases = ["reverse proxy", "home server", "smart home"]
    return strong, weak, phrases


@pytest.fixture
def ai_keywords():
    """Minimal AI/LLM keywords for isolated tests."""
    strong = ["machine-learning", "pytorch", "tensorflow", "llm"]
    weak = ["ai", "ml", "neural", "model"]
    phrases = ["machine learning", "deep learning", "large language"]
    return strong, weak, phrases


# ── STAR-GUIDE content for pipeline tests ───────────────────────

@pytest.fixture
def star_guide_content():
    """Minimal STAR-GUIDE for testing insert and dry-run logic."""
    return """# STAR//GUIDE

My curated stars.

# Part I: The Catalog

## 📡 Homelab Infrastructure

- [existing/tool](https://github.com/existing/tool) — existing entry

## 🤖 Agentic Dev Tools

- [another/repo](https://github.com/another/repo) — another entry

# Part II

## Homelab Top 10

Some content.
"""


@pytest.fixture
def tmp_star_guide(tmp_path, star_guide_content):
    """A real temp file with STAR-GUIDE content for dry-run tests."""
    path = tmp_path / "STAR-GUIDE.md"
    path.write_text(star_guide_content, encoding="utf-8")
    return path


@pytest.fixture
def tmp_not_curated(tmp_path):
    """A temp NOT-CURATED.md for testing removal logic."""
    path = tmp_path / "NOT-CURATED.md"
    path.write_text("""# NOT CURATED

## Existing

- [keep/me](https://github.com/keep/me) — keep this
- [nginx/proxy-manager](https://github.com/nginx/proxy-manager) — remove this
""", encoding="utf-8")
    return path
