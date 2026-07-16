"""Tests for the categories.py loader module."""
import json
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

from categories import (
    load_categories,
    _load_raw,
    _validate,
    _to_4tuple,
    _to_5tuple,
    CATEGORY_KEYWORDS,
    CATEGORY_KEYWORDS_WITH_PHRASES,
    CATEGORY_DICTS,
    get_category_names,
)


# ── Loading ─────────────────────────────────────────────────────

class TestLoadCategories:
    """The load_categories function reads from categories.json."""

    def test_loads_all_categories(self):
        """Should load all 16 categories."""
        cats = load_categories()
        assert len(cats) == 16

    def test_each_category_has_required_keys(self):
        """Every category dict has emoji, name, strong, weak, phrases."""
        cats = load_categories()
        required = {"emoji", "name", "strong", "weak", "phrases"}
        for cat in cats:
            assert required <= cat.keys()

    def test_each_category_has_nonempty_strong(self):
        """Every category should have at least some strong keywords."""
        cats = load_categories()
        for cat in cats:
            assert len(cat["strong"]) > 0, f"{cat['name']} has empty strong keywords"

    def test_each_category_has_nonempty_weak(self):
        """Every category should have at least some weak keywords."""
        cats = load_categories()
        for cat in cats:
            assert len(cat["weak"]) > 0, f"{cat['name']} has empty weak keywords"


# ── 4-tuple export (backward compatible) ────────────────────────

class TestCategoryKeywordTuples:
    """The CATEGORY_KEYWORDS export is a list of 4-tuples."""

    def test_has_16_categories(self):
        assert len(CATEGORY_KEYWORDS) == 16

    def test_all_are_4_tuples(self):
        for tup in CATEGORY_KEYWORDS:
            assert len(tup) == 4
            emoji, name, strong, weak = tup
            assert isinstance(emoji, str)
            assert isinstance(name, str)
            assert isinstance(strong, list)
            assert isinstance(weak, list)

    def test_names_match_json_categories(self):
        """The category names should match what's in categories.json."""
        cats = load_categories()
        expected = [c["name"] for c in cats]
        actual = [t[1] for t in CATEGORY_KEYWORDS]
        assert actual == expected


# ── 5-tuple export ──────────────────────────────────────────────

class TestCategoryKeywordsWithPhrases:
    """The CATEGORY_KEYWORDS_WITH_PHRASES export includes phrases."""

    def test_has_16_categories(self):
        assert len(CATEGORY_KEYWORDS_WITH_PHRASES) == 16

    def test_all_are_5_tuples(self):
        for tup in CATEGORY_KEYWORDS_WITH_PHRASES:
            assert len(tup) == 5
            emoji, name, strong, weak, phrases = tup
            assert isinstance(emoji, str)
            assert isinstance(name, str)
            assert isinstance(strong, list)
            assert isinstance(weak, list)
            assert isinstance(phrases, list)


# ── Utility functions ───────────────────────────────────────────

class TestGetCategoryNames:
    """The get_category_names helper."""

    def test_returns_16_names(self):
        names = get_category_names()
        assert len(names) == 16
        assert all(isinstance(n, str) for n in names)

    def test_includes_expected_categories(self):
        names = get_category_names()
        assert "Homelab Infrastructure" in names
        assert "Agentic Dev Tools" in names
        assert "AI / LLM Tools" in names
        assert "Security & Authentication" in names


# ── Derived helpers ─────────────────────────────────────────────

class TestDerivedHelpers:
    """_to_4tuple and _to_5tuple conversion functions."""

    def test_to_4tuple_converts_correctly(self):
        cat = {
            "emoji": "📡",
            "name": "Test Category",
            "strong": ["kw1", "kw2"],
            "weak": ["kw3"],
            "phrases": ["test phrase"]
        }
        result = _to_4tuple(cat)
        assert result == ("📡", "Test Category", ["kw1", "kw2"], ["kw3"])

    def test_to_5tuple_converts_correctly(self):
        cat = {
            "emoji": "📡",
            "name": "Test Category",
            "strong": ["kw1", "kw2"],
            "weak": ["kw3"],
            "phrases": ["test phrase"]
        }
        result = _to_5tuple(cat)
        assert result == ("📡", "Test Category", ["kw1", "kw2"], ["kw3"], ["test phrase"])


# ── Validation ──────────────────────────────────────────────────

class TestValidate:
    """The _validate function checks category structure."""

    def test_valid_category_passes(self):
        assert _validate({
            "emoji": "📡",
            "name": "Test",
            "strong": ["kw1"],
            "weak": ["kw2"],
            "phrases": ["test phrase"]
        }) is True

    def test_missing_key_fails(self):
        assert _validate({
            "emoji": "📡",
            "name": "Test",
            "strong": ["kw1"],
        }) is False

    def test_non_list_keywords_fails(self):
        assert _validate({
            "emoji": "📡",
            "name": "Test",
            "strong": "not-a-list",
            "weak": ["kw2"],
            "phrases": []
        }) is False

    def test_non_list_phrases_fails(self):
        assert _validate({
            "emoji": "📡",
            "name": "Test",
            "strong": ["kw1"],
            "weak": ["kw2"],
            "phrases": "not-a-list"
        }) is False

    def test_empty_string_emoji_passes(self):
        """Even empty emoji is a string, so it passes type check."""
        assert _validate({
            "emoji": "",
            "name": "Test",
            "strong": ["kw1"],
            "weak": ["kw2"],
            "phrases": []
        }) is True


# ── Dict export ──────────────────────────────────────────────────

class TestCategoryDicts:
    """CATEGORY_DICTS provides full dict access."""

    def test_has_all_16(self):
        assert len(CATEGORY_DICTS) == 16

    def test_dicts_have_all_keys(self):
        for d in CATEGORY_DICTS:
            for key in ("emoji", "name", "strong", "weak", "phrases"):
                assert key in d
