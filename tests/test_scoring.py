"""Tests for score_repo_for_category: phrase matching, star bonus, edge cases."""
import pytest
from update_stars import score_repo_for_category, tokenize
from categories import CATEGORY_KEYWORDS_WITH_PHRASES


class TestTokenize:
    def test_simple_tokens(self):
        assert tokenize("Hello World") == {"hello", "world"}
    def test_hyphenated_kept(self):
        tokens = tokenize("self-host nginx-proxy-manager")
        assert "self-host" in tokens
    def test_punctuation_stripped(self):
        tokens = tokenize("hello, world! node.js")
        assert "hello" in tokens
        assert "node" in tokens
    def test_empty_string(self):
        assert tokenize("") == set()
    def test_none_input(self):
        assert tokenize(None) == set()


class TestBasicScoring:
    def test_strong_keyword_exact_match(self):
        score = score_repo_for_category(
            "user/my-self-host-app", "Python", "A cool tool for self-host",
            ["self-host"], [], phrases=None, stars=0)
        assert score == 4  # self-host not standalone in my-self-host-app
    def test_strong_keyword_substring_fallback(self):
        score = score_repo_for_category(
            "user/randomrepo", "Python", "something about tailscale vpn",
            ["tailscale"], [], phrases=None, stars=0)
        assert score == 4
    def test_weak_keyword_exact_match(self):
        score = score_repo_for_category(
            "user/server-app", "Go", "A simple server",
            [], ["server"], phrases=None, stars=0)
        assert score == 1  # server not standalone in server-app
    def test_weak_keyword_substring(self):
        score = score_repo_for_category(
            "user/my-repo", "Python", "A dashboard for homelab servers",
            [], ["dashboard"], phrases=None, stars=0)
        assert score == 1
    def test_no_match(self):
        score = score_repo_for_category(
            "user/xyz", "Rust", "completely unrelated",
            ["homelab"], ["server"], phrases=None, stars=0)
        assert score == 0

class TestPhraseMatching:
    def test_phrase_in_description(self, homelab_keywords):
        strong, weak, phrases = homelab_keywords
        score = score_repo_for_category("tools/nginx-config", "Shell", "Nginx reverse proxy configuration tool", strong, weak, phrases=phrases, stars=0)
        assert score >= 3
    def test_phrase_in_name(self, homelab_keywords):
        strong, weak, phrases = homelab_keywords
        score = score_repo_for_category("user/reverse-proxy-manager", "Go", "A proxy management tool", strong, weak, phrases=phrases, stars=0)
        assert score >= 2  # reverse-proxy != reverse proxy as phrase
    def test_phrase_delta(self, homelab_keywords):
        strong, weak, phrases = homelab_keywords
        s1 = score_repo_for_category("user/homelab-dashboard", "Python", "A home server dashboard with smart home integration", strong, weak, phrases=phrases, stars=0)
        s2 = score_repo_for_category("user/homelab-dashboard", "Python", "A home server dashboard with smart home integration", strong, weak, phrases=None, stars=0)
        assert s1 > s2
        assert s1 - s2 >= 3
    def test_phrases_none_safe(self, homelab_keywords):
        strong, weak, _ = homelab_keywords
        score = score_repo_for_category("user/tool", "Python", "desc", strong, weak, phrases=None, stars=0)
        assert score >= 0
    def test_phrases_empty_list(self, homelab_keywords):
        strong, weak, _ = homelab_keywords
        score = score_repo_for_category("user/tool", "Python", "desc", strong, weak, phrases=[], stars=0)
        assert score >= 0


class TestStarBonus:
    strong = ["homelab", "self-host"]
    weak = ["server"]
    def _s(self, stars):
        return score_repo_for_category("test/homelab-tool", "Python", "A self-hosted homelab tool", self.strong, self.weak, phrases=None, stars=stars)
    def test_zero_stars_no_bonus(self):
        assert self._s(0) >= 0
    def test_below_threshold_no_bonus(self):
        assert self._s(19000) == self._s(0)
        assert self._s(1000) == self._s(0)
    def test_20k_gives_plus_1(self):
        assert self._s(20000) - self._s(0) == 1
    def test_50k_gives_plus_2(self):
        assert self._s(50000) - self._s(0) == 2
    def test_100k_caps_at_5(self):
        assert self._s(100000) - self._s(0) == 5
    def test_200k_still_capped_at_5(self):
        assert self._s(100000) == self._s(200000)
    def test_none_stars_safe(self):
        score = score_repo_for_category("user/tool", "Python", "desc", self.strong, self.weak, phrases=None, stars=None)
        assert score >= 0


class TestPluralStemming:
    """Plural stemming: keywords match token+s forms (e.g. LLM→LLMs)."""

    def test_strong_keyword_plural_in_desc(self):
        """'LLM' should match 'LLMs' as a token (plural stemming)."""
        score = score_repo_for_category(
            "qualcomm/GenieX", "Rust", "Run frontier LLMs and VLMs locally",
            ["llm"], [], phrases=None, stars=0)
        assert score >= 4  # LLM+s → LLMs token match = 4 pts

    def test_strong_keyword_plural_in_name(self):
        """'agent' should match 'agents' in repo name."""
        score = score_repo_for_category(
            "user/agents", "Python", "Some tool",
            ["agent"], [], phrases=None, stars=0)
        # agent+s → agents in name token = 4 + 2 bonus = 6
        assert score >= 6

    def test_weak_keyword_plural_in_desc(self):
        """'model' weak keyword should match 'models' via plural stemming."""
        score = score_repo_for_category(
            "user/tool", "Python", "Trains models and ships ML models",
            [], ["model"], phrases=None, stars=0)
        assert score >= 1  # model+s → models token match = 1 pt

    def test_strong_keyword_plural_token_match(self):
        """Substring fallback also checks kw+s form."""
        score = score_repo_for_category(
            "user/repo", "Go", "something about LLMs in production",
            ["llm"], [], phrases=None, stars=0)
        assert score >= 4  # token match via plural stemming (llm+s=llms)
        # The description tokenizes 'LLMs' → 'llms', so kw+s matches as token

    def test_no_false_positive_on_unrelated_plural(self):
        """Words ending in 's' naturally shouldn't false-match."""
        score = score_repo_for_category(
            "user/bus-app", "TypeScript", "A bus tracking application with regular English words",
            ["xyz"], [], phrases=None, stars=0)
        # 'xyz'+s = 'xyzs' which should not match anything in the text
        assert score == 0


class TestEdgeCases:
    def test_empty_description(self):
        score = score_repo_for_category("user/repo", "Python", "", ["python"], ["tool"], phrases=None, stars=100)
        assert score >= 0
    def test_none_description(self):
        score = score_repo_for_category("user/repo", "Python", None, ["python"], ["tool"], phrases=None, stars=0)
        assert score >= 0
    def test_repo_name_without_slash(self):
        score = score_repo_for_category("standalone-repo", "Go", "A self-host tool", ["self-host"], [], phrases=None, stars=0)
        assert score >= 4
    def test_empty_keywords(self):
        score = score_repo_for_category("user/repo", "Python", "description", [], [], phrases=None, stars=0)
        assert score == 0
