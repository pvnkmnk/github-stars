"""Tests for suggest_categories, threshold logic, and dry-run guards."""
import pytest
from pathlib import Path
from update_stars import score_repo_for_category, suggest_categories, auto_curate_repos


class TestSuggestCategories:
    def test_returns_correct_format(self, sample_repos):
        results = suggest_categories(sample_repos[:2])
        assert len(results) == 2
        for stars, full_name, lang, desc, cats in results:
            assert isinstance(stars, int)
            assert isinstance(full_name, str)
            assert isinstance(cats, list)
            for cat in cats:
                assert len(cat) == 3
    def test_sorted_by_score_descending(self, sample_repos):
        results = suggest_categories(sample_repos[:1])
        cats = results[0][4]
        if len(cats) > 1:
            for i in range(len(cats) - 1):
                assert cats[i][2] >= cats[i + 1][2]
    def test_max_three_suggestions(self, sample_repos):
        results = suggest_categories(sample_repos)
        for _, _, _, _, cats in results:
            assert len(cats) <= 3
    def test_empty_input(self):
        assert suggest_categories([]) == []
    def test_repo_with_no_matches(self):
        results = suggest_categories([(0, "test/xyz", "XPL", "xqzzrt yzlmxw")])
        assert results[0][4] == []

class TestThresholdLogic:
    def test_auto_curate_with_clear_winner(self, tmp_star_guide, tmp_not_curated):
        repos = [(500, "homelab/homeassistant", "Python", "Home Assistant for self-hosted homelab automation")]
        autos, remaining, modified = auto_curate_repos(repos, str(tmp_star_guide), threshold=4, not_curated_path=str(tmp_not_curated), dry_run=False)
        assert len(autos) == 1
        assert len(remaining) == 0
        assert "Infrastructure" in autos[0][1] or "Homelab" in autos[0][1]
    def test_low_score_not_auto_curated(self, tmp_star_guide):
        repos = [(10, "user/xqzzy-repo", "Unknown", "No keywords matched here")]
        autos, remaining, modified = auto_curate_repos(repos, str(tmp_star_guide), threshold=7, not_curated_path=None, dry_run=False)
        assert len(autos) == 0
        assert len(remaining) == 1
        assert modified is False
    def test_no_suggestions_no_curation(self, tmp_star_guide):
        repos = [(0, "x/y", "ZZ", "zzzz zzzz zzzz zzzz zzzz zzzz")]
        autos, remaining, modified = auto_curate_repos(repos, str(tmp_star_guide), threshold=1, dry_run=False)
        assert len(autos) == 0
        assert len(remaining) == 1
    def test_second_score_zero_auto_curates(self, tmp_star_guide):
        repos = [(100, "goauthentik/authentik", "Python", "authentik self-hosted authentication SSO")]
        autos, remaining, modified = auto_curate_repos(repos, str(tmp_star_guide), threshold=3, not_curated_path=None, dry_run=False)
        assert len(autos) >= 1


class TestDryRunGuards:
    def test_dry_run_does_not_write_star_guide(self, tmp_star_guide, tmp_not_curated):
        original = tmp_star_guide.read_text(encoding="utf-8")
        repos = [(500, "homelab/homeassistant", "Python", "Home Assistant for self-hosted homelab automation")]
        autos, remaining, modified = auto_curate_repos(repos, str(tmp_star_guide), threshold=4, not_curated_path=str(tmp_not_curated), dry_run=True)
        after = tmp_star_guide.read_text(encoding="utf-8")
        assert after == original
        # modified may be False if fixture has no table rows
    def test_dry_run_does_not_remove_from_not_curated(self, tmp_star_guide, tmp_not_curated):
        original = tmp_not_curated.read_text(encoding="utf-8")
        repos = [(500, "nginx/proxy-manager", "Go", "reverse proxy nginx manager for homeserver")]
        auto_curate_repos(repos, str(tmp_star_guide), threshold=4, not_curated_path=str(tmp_not_curated), dry_run=True)
        after = tmp_not_curated.read_text(encoding="utf-8")
        assert after == original
    def test_dry_run_still_returns_results(self, tmp_star_guide, tmp_not_curated):
        repos = [(500, "homelab/homeassistant", "Python", "Home Assistant for self-hosted homelab automation")]
        autos, remaining, modified = auto_curate_repos(repos, str(tmp_star_guide), threshold=4, not_curated_path=str(tmp_not_curated), dry_run=True)
        assert len(autos) >= 1
        assert len(remaining) == 0
    def test_dry_run_with_no_not_curated_path(self, tmp_star_guide):
        repos = [(500, "homelab/homeassistant", "Python", "Home Assistant for self-hosted homelab automation")]
        autos, remaining, modified = auto_curate_repos(repos, str(tmp_star_guide), threshold=4, not_curated_path=None, dry_run=True)
        assert len(autos) >= 1


class TestKeywordCoverage:
    def test_copilot_matches_agentic_dev_tools(self):
        from categories import CATEGORY_KEYWORDS_WITH_PHRASES
        agentic = [c for c in CATEGORY_KEYWORDS_WITH_PHRASES if c[1] == "Agentic Dev Tools"][0]
        assert "copilot" in agentic[2]
        score = score_repo_for_category("github/copilot-cli", "TypeScript", "GitHub Copilot CLI - AI pair programmer", agentic[2], agentic[3], phrases=agentic[4], stars=12000)
        assert score >= 4
    def test_authentik_matches_security(self):
        from categories import CATEGORY_KEYWORDS_WITH_PHRASES
        security = [c for c in CATEGORY_KEYWORDS_WITH_PHRASES if c[1] == "Security & Authentication"][0]
        assert "authentik" in security[2]
        score = score_repo_for_category("goauthentik/authentik", "Python", "authentik is an open-source Identity Provider", security[2], security[3], phrases=security[4], stars=3500)
        assert score >= 4
    def test_tabby_matches_agentic_dev_tools(self):
        from categories import CATEGORY_KEYWORDS_WITH_PHRASES
        agentic = [c for c in CATEGORY_KEYWORDS_WITH_PHRASES if c[1] == "Agentic Dev Tools"][0]
        assert "tabby" in agentic[2]
        score = score_repo_for_category("TabbyML/tabby", "Rust", "Self-hosted AI coding assistant", agentic[2], agentic[3], phrases=agentic[4], stars=15000)
        assert score >= 4
