"""Tests for auto_curate_repos: gap rule, threshold logic, clear-winner detection."""
import pytest
from unittest.mock import patch


def _make_result(stars, full_name, lang, desc, category_scores):
    return (stars, full_name, lang, desc, category_scores)


# Emoji mapping — must match find_section_end header pattern: "## {emoji} "
EMOJI = {
    "Agentic": "🤖",
    "AI": "🧠",
    "Terminal": "⌨️",
    "Web": "🌐",
    "Dev": "💻",
}


def _mock_suggest(repos):
    results = []
    for stars, full_name, lang, desc in repos:
        cat_scores = []
        for part in lang.split(","):
            name, score_str = part.rsplit(":", 1)
            emoji = EMOJI.get(name, "💻")
            cat_scores.append((emoji, name, int(score_str)))
        cat_scores.sort(key=lambda x: -x[2])
        results.append(_make_result(stars, full_name, "Python", desc, cat_scores))
    return results


class TestThresholdLogic:
    """Threshold=7: score >= 7 passes, < 7 rejected."""

    def test_above_threshold_passes(self, tmp_path):
        from update_stars import auto_curate_repos
        sg = tmp_path / "STAR-GUIDE.md"
        sg.write_text("# Part I: The Catalog\n\n## 💻 Dev Tools & Languages\n\n", encoding="utf-8")
        repos = [(1000, "user/good-tool", "Dev:7", "A great tool")]
        with patch("update_stars.suggest_categories", side_effect=_mock_suggest):
            curated, remaining, modified = auto_curate_repos(repos, str(sg), threshold=7, dry_run=True)
        assert len(curated) == 1
        assert curated[0][4] == "user/good-tool"  # full_name is index 4

    def test_below_threshold_rejected(self, tmp_path):
        from update_stars import auto_curate_repos
        sg = tmp_path / "STAR-GUIDE.md"
        sg.write_text("# Part I: The Catalog\n\n## 💻 Dev Tools & Languages\n\n", encoding="utf-8")
        repos = [(500, "user/weak-tool", "Dev:6", "Almost good")]
        with patch("update_stars.suggest_categories", side_effect=_mock_suggest):
            curated, remaining, modified = auto_curate_repos(repos, str(sg), threshold=7, dry_run=True)
        assert len(curated) == 0
        assert remaining[0][1] == "user/weak-tool"

    def test_exactly_at_threshold_passes(self, tmp_path):
        from update_stars import auto_curate_repos
        sg = tmp_path / "STAR-GUIDE.md"
        sg.write_text("# Part I: The Catalog\n\n## ⌨️ Terminal, CLI & Shell\n\n", encoding="utf-8")
        repos = [(300, "user/cli-tool", "Terminal:7", "A CLI tool")]
        with patch("update_stars.suggest_categories", side_effect=_mock_suggest):
            curated, remaining, modified = auto_curate_repos(repos, str(sg), threshold=7, dry_run=True)
        assert len(curated) == 1


class TestUnambiguousCategory:
    """Single category with score >= threshold → auto-curate (no ambiguity)."""

    def test_single_category_auto_curates(self, tmp_path):
        from update_stars import auto_curate_repos
        sg = tmp_path / "STAR-GUIDE.md"
        sg.write_text("# Part I: The Catalog\n\n## 🧠 AI / LLM Tools\n\n", encoding="utf-8")
        repos = [(8000, "user/ai-model", "AI:7", "An AI model")]
        with patch("update_stars.suggest_categories", side_effect=_mock_suggest):
            curated, remaining, modified = auto_curate_repos(repos, str(sg), threshold=7, dry_run=True)
        assert len(curated) == 1
        assert len(remaining) == 0


class TestHighConfidenceFloatingGap:
    """Floating gap: score >= threshold+4 (11) ignores regular gap check."""

    def test_high_confidence_ignores_tight_gap(self, tmp_path):
        from update_stars import auto_curate_repos
        sg = tmp_path / "STAR-GUIDE.md"
        sg.write_text("# Part I: The Catalog\n\n## 🤖 Agentic Dev Tools\n\n", encoding="utf-8")
        repos = [(5000, "user/high-conf", "Agentic:11,Dev:10", "High confidence match")]
        with patch("update_stars.suggest_categories", side_effect=_mock_suggest):
            curated, remaining, modified = auto_curate_repos(repos, str(sg), threshold=7, dry_run=True)
        assert len(curated) == 1
        assert curated[0][1] == "Agentic"  # cat_name is index 1

    def test_exactly_threshold_plus_4(self, tmp_path):
        from update_stars import auto_curate_repos
        sg = tmp_path / "STAR-GUIDE.md"
        sg.write_text("# Part I: The Catalog\n\n## 🤖 Agentic Dev Tools\n\n", encoding="utf-8")
        repos = [(2000, "user/borderline", "Agentic:11,Dev:10", "Borderline high conf")]
        with patch("update_stars.suggest_categories", side_effect=_mock_suggest):
            curated, remaining, modified = auto_curate_repos(repos, str(sg), threshold=7, dry_run=True)
        assert len(curated) == 1

    def test_just_below_floating_gap_checks_regular_gap(self, tmp_path):
        from update_stars import auto_curate_repos
        sg = tmp_path / "STAR-GUIDE.md"
        sg.write_text("# Part I: The Catalog\n\n## 💻 Dev Tools & Languages\n\n", encoding="utf-8")
        repos = [(1500, "user/good-gap", "Dev:10,Web:8", "Good gap 1.25x")]
        with patch("update_stars.suggest_categories", side_effect=_mock_suggest):
            curated, remaining, modified = auto_curate_repos(repos, str(sg), threshold=7, dry_run=True)
        assert len(curated) == 1


class TestGapRule:
    """Gap rule: top_score >= 1.15 * second_score is required when < threshold+4."""

    def test_clear_gap_passes(self, tmp_path):
        from update_stars import auto_curate_repos
        sg = tmp_path / "STAR-GUIDE.md"
        sg.write_text("# Part I: The Catalog\n\n## 🤖 Agentic Dev Tools\n\n", encoding="utf-8")
        repos = [(2000, "user/clear-win", "Agentic:9,Dev:6", "Clear winner 1.5x")]
        with patch("update_stars.suggest_categories", side_effect=_mock_suggest):
            curated, remaining, modified = auto_curate_repos(repos, str(sg), threshold=7, dry_run=True)
        assert len(curated) == 1

    def test_gap_boundary_passes(self, tmp_path):
        """7/6 = 1.167x > 1.15 → passes."""
        from update_stars import auto_curate_repos
        sg = tmp_path / "STAR-GUIDE.md"
        sg.write_text("# Part I: The Catalog\n\n## ⌨️ Terminal, CLI & Shell\n\n", encoding="utf-8")
        repos = [(500, "user/borderline-gap", "Terminal:7,Dev:6", "Borderline gap 1.17x")]
        with patch("update_stars.suggest_categories", side_effect=_mock_suggest):
            curated, remaining, modified = auto_curate_repos(repos, str(sg), threshold=7, dry_run=True)
        assert len(curated) == 1

    def test_tied_rejected(self, tmp_path):
        """7/7 = 1.0x < 1.15 → rejected."""
        from update_stars import auto_curate_repos
        sg = tmp_path / "STAR-GUIDE.md"
        sg.write_text("# Part I: The Catalog\n\n## 💻 Dev Tools & Languages\n\n", encoding="utf-8")
        repos = [(1000, "user/tied", "Dev:7,Agentic:7", "Tied categories")]
        with patch("update_stars.suggest_categories", side_effect=_mock_suggest):
            curated, remaining, modified = auto_curate_repos(repos, str(sg), threshold=7, dry_run=True)
        assert len(curated) == 0

    def test_narrow_loss_rejected(self, tmp_path):
        """8/7 = 1.143x < 1.15 → rejected."""
        from update_stars import auto_curate_repos
        sg = tmp_path / "STAR-GUIDE.md"
        sg.write_text("# Part I: The Catalog\n\n## 🤖 Agentic Dev Tools\n\n", encoding="utf-8")
        repos = [(80000, "user/narrow-loss", "Agentic:8,Dev:7", "Close but not clear 1.14x")]
        with patch("update_stars.suggest_categories", side_effect=_mock_suggest):
            curated, remaining, modified = auto_curate_repos(repos, str(sg), threshold=7, dry_run=True)
        assert len(curated) == 0

    def test_ponytail_case_passes(self, tmp_path):
        """9/7 = 1.286x > 1.15 → passes (the real ponytail scenario)."""
        from update_stars import auto_curate_repos
        sg = tmp_path / "STAR-GUIDE.md"
        sg.write_text("# Part I: The Catalog\n\n## 🤖 Agentic Dev Tools\n\n", encoding="utf-8")
        repos = [(84000, "user/ponytail", "Agentic:9,Dev:7", "Ponytail-like 1.29x gap")]
        with patch("update_stars.suggest_categories", side_effect=_mock_suggest):
            curated, remaining, modified = auto_curate_repos(repos, str(sg), threshold=7, dry_run=True)
        assert len(curated) == 1


class TestMultipleRepos:
    """Multiple repos: 2 pass, 2 fail based on threshold and gap."""

    def test_mixed_results(self, tmp_path):
        from update_stars import auto_curate_repos
        sg = tmp_path / "STAR-GUIDE.md"
        sg.write_text(
            "# Part I: The Catalog\n\n## 🤖 Agentic Dev Tools\n\n## 💻 Dev Tools & Languages\n\n## ⌨️ Terminal, CLI & Shell\n\n",
            encoding="utf-8",
        )
        repos = [
            (1000, "user/pass1", "Agentic:9,Dev:5", "Clear win 1.8x"),
            (2000, "user/fail1", "Dev:7,Agentic:7", "Tied 1.0x"),
            (3000, "user/pass2", "Terminal:8,Dev:6", "Decent gap 1.33x"),
            (4000, "user/fail2", "Web:6", "Below threshold"),
        ]
        with patch("update_stars.suggest_categories", side_effect=_mock_suggest):
            curated, remaining, modified = auto_curate_repos(repos, str(sg), threshold=7, dry_run=True)
        assert len(curated) == 2
        names = [c[4] for c in curated]  # full_name is index 4
        assert "user/pass1" in names
        assert "user/pass2" in names
        assert len(remaining) == 2


class TestCustomThreshold:
    """Threshold can be adjusted: lower catches more, higher blocks more."""

    def test_threshold_5_catches_more(self, tmp_path):
        from update_stars import auto_curate_repos
        sg = tmp_path / "STAR-GUIDE.md"
        sg.write_text("# Part I: The Catalog\n\n## 💻 Dev Tools & Languages\n\n", encoding="utf-8")
        repos = [(300, "user/medium", "Dev:6", "Medium score")]
        with patch("update_stars.suggest_categories", side_effect=_mock_suggest):
            curated, remaining, modified = auto_curate_repos(repos, str(sg), threshold=5, dry_run=True)
        assert len(curated) == 1

    def test_threshold_10_blocks_more(self, tmp_path):
        from update_stars import auto_curate_repos
        sg = tmp_path / "STAR-GUIDE.md"
        sg.write_text("# Part I: The Catalog\n\n## 🧠 AI / LLM Tools\n\n", encoding="utf-8")
        repos = [(5000, "user/good", "AI:8", "Good AI tool")]
        with patch("update_stars.suggest_categories", side_effect=_mock_suggest):
            curated, remaining, modified = auto_curate_repos(repos, str(sg), threshold=10, dry_run=True)
        assert len(curated) == 0


class TestDryRun:
    """dry_run=True should not write to disk; dry_run=False should."""

    def test_dry_run_does_not_write(self, tmp_path):
        from update_stars import auto_curate_repos
        sg = tmp_path / "STAR-GUIDE.md"
        original = (
            "# Part I: The Catalog\n\n"
            "## 🤖 Agentic Dev Tools\n\n"
            "| Repository | Stars | Language | Description | Status |\n"
            "|------------|-------|----------|-------------|--------|\n"
            "| [existing/repo](https://github.com/existing/repo) | 1,000 | Python | Existing tool | ✅ |\n"
            "\n"
        )
        sg.write_text(original, encoding="utf-8")
        repos = [(5000, "user/new-tool", "Agentic:9,Dev:5", "Clear win")]
        with patch("update_stars.suggest_categories", side_effect=_mock_suggest):
            curated, remaining, modified = auto_curate_repos(repos, str(sg), threshold=7, dry_run=True)
        assert sg.read_text(encoding="utf-8") == original
        assert modified is True  # section found, content was modified in memory

    def test_non_dry_run_writes(self, tmp_path):
        from update_stars import auto_curate_repos
        sg = tmp_path / "STAR-GUIDE.md"
        original = (
            "# Part I: The Catalog\n\n"
            "## 🤖 Agentic Dev Tools\n\n"
            "| Repository | Stars | Language | Description | Status |\n"
            "|------------|-------|----------|-------------|--------|\n"
            "| [existing/repo](https://github.com/existing/repo) | 1,000 | Python | Existing tool | ✅ |\n"
            "\n"
        )
        sg.write_text(original, encoding="utf-8")
        repos = [(5000, "user/new-tool", "Agentic:9,Dev:5", "Clear win")]
        with patch("update_stars.suggest_categories", side_effect=_mock_suggest):
            curated, remaining, modified = auto_curate_repos(repos, str(sg), threshold=7, dry_run=False)
        content = sg.read_text(encoding="utf-8")
        assert "user/new-tool" in content
        assert content != original
        assert modified is True

class TestRemoveFromNotCurated:
    """Unit tests for remove_from_not_curated directly."""

    def test_removes_matching_lines(self, tmp_path):
        from update_stars import remove_from_not_curated
        nc = tmp_path / "NOT-CURATED.md"
        nc.write_text(
            "# Not Curated\n\n"
            "## June 2026\n\n"
            "- [user/tool1](https://github.com/user/tool1) — Interesting tool\n"
            "- [user/tool2](https://github.com/user/tool2) — Another one\n"
            "- [user/tool3](https://github.com/user/tool3) — Keep this\n",
            encoding="utf-8",
        )
        removed = remove_from_not_curated({"user/tool1", "user/tool2"}, str(nc))
        assert removed == 2
        result = nc.read_text(encoding="utf-8")
        assert "user/tool1" not in result
        assert "user/tool2" not in result
        assert "user/tool3" in result

    def test_no_matches_returns_zero(self, tmp_path):
        from update_stars import remove_from_not_curated
        nc = tmp_path / "NOT-CURATED.md"
        original = "# Not Curated\n\n- [user/keep](https://github.com/user/keep) — Keep\n"
        nc.write_text(original, encoding="utf-8")
        removed = remove_from_not_curated({"user/other"}, str(nc))
        assert removed == 0
        assert nc.read_text(encoding="utf-8") == original

    def test_missing_file_returns_zero(self, tmp_path):
        from update_stars import remove_from_not_curated
        nc = tmp_path / "NONEXISTENT.md"
        removed = remove_from_not_curated({"user/any"}, str(nc))
        assert removed == 0

    def test_empty_repo_names_removes_nothing(self, tmp_path):
        from update_stars import remove_from_not_curated
        nc = tmp_path / "NOT-CURATED.md"
        original = "# Not Curated\n\n- [user/keep](https://github.com/user/keep) — Keep\n"
        nc.write_text(original, encoding="utf-8")
        removed = remove_from_not_curated(set(), str(nc))
        assert removed == 0

    def test_preserves_non_repo_lines(self, tmp_path):
        from update_stars import remove_from_not_curated
        nc = tmp_path / "NOT-CURATED.md"
        original = (
            "# Not Curated\n\n"
            "## June 2026\n\n"
            "Some intro text here.\n\n"
            "- [user/remove](https://github.com/user/remove) — Remove me\n"
            "- Not a repo line\n"
            "- [user/keep](https://github.com/user/keep) — Keep\n"
            "\n"
            "Footer text\n"
        )
        nc.write_text(original, encoding="utf-8")
        removed = remove_from_not_curated({"user/remove"}, str(nc))
        assert removed == 1
        result = nc.read_text(encoding="utf-8")
        assert "user/remove" not in result
        assert "user/keep" in result
        assert "Some intro text" in result
        assert "Not a repo line" in result
        assert "Footer text" in result


class TestNotCuratedPath:
    """not_curated_path parameter: removes curated repos from NOT-CURATED.md."""

    def test_none_path_does_nothing(self, tmp_path):
        from update_stars import auto_curate_repos
        sg = tmp_path / "STAR-GUIDE.md"
        sg.write_text(
            "# Part I: The Catalog\n\n"
            "## 🤖 Agentic Dev Tools\n\n"
            "| Repository | Stars | Language | Description | Status |\n"
            "|------------|-------|----------|-------------|--------|\n"
            "| [existing/repo](https://github.com/existing/repo) | 1,000 | Python | Existing | ✅ |\n\n",
            encoding="utf-8",
        )
        repos = [(5000, "user/curated-tool", "Agentic:9,Dev:5", "Clear win")]
        with patch("update_stars.suggest_categories", side_effect=_mock_suggest):
            curated, remaining, modified = auto_curate_repos(
                repos, str(sg), threshold=7, not_curated_path=None, dry_run=False
            )
        assert len(curated) == 1
        assert curated[0][4] == "user/curated-tool"
        assert modified is True

    def test_dry_run_preserves_not_curated_file(self, tmp_path):
        from update_stars import auto_curate_repos
        sg = tmp_path / "STAR-GUIDE.md"
        nc = tmp_path / "NOT-CURATED.md"
        original_nc = "# Not Curated\n\n- [user/will-curate](https://github.com/user/will-curate) — Soon\n"
        nc.write_text(original_nc, encoding="utf-8")
        sg.write_text(
            "# Part I: The Catalog\n\n"
            "## 🧠 AI / LLM Tools\n\n"
            "| Repository | Stars | Language | Description | Status |\n"
            "|------------|-------|----------|-------------|--------|\n"
            "| [existing/repo](https://github.com/existing/repo) | 1,000 | Python | Existing | ✅ |\n\n",
            encoding="utf-8",
        )
        repos = [(8000, "user/will-curate", "AI:11,Dev:5", "High confidence")]
        with patch("update_stars.suggest_categories", side_effect=_mock_suggest):
            curated, remaining, modified = auto_curate_repos(
                repos, str(sg), threshold=7, not_curated_path=str(nc), dry_run=True
            )
        assert len(curated) == 1
        assert nc.read_text(encoding="utf-8") == original_nc
        assert modified is True

    def test_removes_curated_repos_from_not_curated(self, tmp_path):
        from update_stars import auto_curate_repos
        sg = tmp_path / "STAR-GUIDE.md"
        nc = tmp_path / "NOT-CURATED.md"
        nc.write_text(
            "# Not Curated\n\n"
            "## July 2026\n\n"
            "- [user/auto-me](https://github.com/user/auto-me) — Auto-curate me\n"
            "- [user/stay-here](https://github.com/user/stay-here) — Stay in NOT-CURATED\n"
            "- [user/also-curated](https://github.com/user/also-curated) — Me too\n\n"
            "Footer.\n",
            encoding="utf-8",
        )
        sg.write_text(
            "# Part I: The Catalog\n\n"
            "## 🤖 Agentic Dev Tools\n\n"
            "| Repository | Stars | Language | Description | Status |\n"
            "|------------|-------|----------|-------------|--------|\n"
            "| [existing/repo](https://github.com/existing/repo) | 1,000 | Python | Existing | ✅ |\n\n",
            encoding="utf-8",
        )
        repos = [
            (5000, "user/auto-me", "Agentic:9,Dev:5", "Clear winner"),
            (3000, "user/also-curated", "Agentic:8,Dev:6", "Good gap"),
        ]
        with patch("update_stars.suggest_categories", side_effect=_mock_suggest):
            curated, remaining, modified = auto_curate_repos(
                repos, str(sg), threshold=7, not_curated_path=str(nc), dry_run=False
            )
        assert len(curated) == 2
        assert modified is True
        result = nc.read_text(encoding="utf-8")
        assert "user/auto-me" not in result
        assert "user/also-curated" not in result
        assert "user/stay-here" in result
        assert "Footer" in result

    def test_missing_not_curated_file_no_error(self, tmp_path):
        from update_stars import auto_curate_repos
        sg = tmp_path / "STAR-GUIDE.md"
        nc = tmp_path / "DOES-NOT-EXIST.md"
        sg.write_text(
            "# Part I: The Catalog\n\n"
            "## 🧠 AI / LLM Tools\n\n"
            "| Repository | Stars | Language | Description | Status |\n"
            "|------------|-------|----------|-------------|--------|\n"
            "| [existing/repo](https://github.com/existing/repo) | 1,000 | Python | Existing | ✅ |\n\n",
            encoding="utf-8",
        )
        repos = [(5000, "user/new-tool", "AI:10,Agentic:5", "Strong AI match")]
        with patch("update_stars.suggest_categories", side_effect=_mock_suggest):
            curated, remaining, modified = auto_curate_repos(
                repos, str(sg), threshold=7, not_curated_path=str(nc), dry_run=False
            )
        assert len(curated) == 1
        assert modified is True
        assert not nc.exists()

    def test_not_curated_repos_preserved_when_not_curated(self, tmp_path):
        from update_stars import auto_curate_repos
        sg = tmp_path / "STAR-GUIDE.md"
        nc = tmp_path / "NOT-CURATED.md"
        original_nc = (
            "# Not Curated\n\n"
            "- [user/not-good-enough](https://github.com/user/not-good-enough) — Too low\n"
        )
        nc.write_text(original_nc, encoding="utf-8")
        sg.write_text(
            "# Part I: The Catalog\n\n"
            "## 🤖 Agentic Dev Tools\n\n"
            "| Repository | Stars | Language | Description | Status |\n"
            "|------------|-------|----------|-------------|--------|\n"
            "| [existing/repo](https://github.com/existing/repo) | 1,000 | Python | Existing | ✅ |\n\n",
            encoding="utf-8",
        )
        repos = [(200, "user/not-good-enough", "Dev:5", "Below threshold")]
        with patch("update_stars.suggest_categories", side_effect=_mock_suggest):
            curated, remaining, modified = auto_curate_repos(
                repos, str(sg), threshold=7, not_curated_path=str(nc), dry_run=False
            )
        assert len(curated) == 0
        assert modified is False
        assert nc.read_text(encoding="utf-8") == original_nc

    def test_partial_curation_leaves_uncurated_in_not_curated(self, tmp_path):
        from update_stars import auto_curate_repos
        sg = tmp_path / "STAR-GUIDE.md"
        nc = tmp_path / "NOT-CURATED.md"
        nc.write_text(
            "# Not Curated\n\n"
            "- [user/curated](https://github.com/user/curated) — Now good enough\n"
            "- [user/still-not](https://github.com/user/still-not) — Still borderline\n",
            encoding="utf-8",
        )
        sg.write_text(
            "# Part I: The Catalog\n\n"
            "## 🧠 AI / LLM Tools\n\n"
            "| Repository | Stars | Language | Description | Status |\n"
            "|------------|-------|----------|-------------|--------|\n"
            "| [existing/repo](https://github.com/existing/repo) | 1,000 | Python | Existing | ✅ |\n\n",
            encoding="utf-8",
        )
        repos = [
            (5000, "user/curated", "AI:9,Dev:5", "Clear win"),
            (100, "user/still-not", "Dev:6", "Still below threshold"),
        ]
        with patch("update_stars.suggest_categories", side_effect=_mock_suggest):
            curated, remaining, modified = auto_curate_repos(
                repos, str(sg), threshold=7, not_curated_path=str(nc), dry_run=False
            )
        assert len(curated) == 1
        assert curated[0][4] == "user/curated"
        result = nc.read_text(encoding="utf-8")
        assert "user/curated" not in result
        assert "user/still-not" in result
        assert modified is True
