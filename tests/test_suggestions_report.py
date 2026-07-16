"""Tests for generate_suggestions_report: CATEGORIZATION-SUGGESTIONS.md generation."""
import pytest
from unittest.mock import patch


def _make_result(stars, full_name, lang, desc, category_scores):
    return (stars, full_name, lang, desc, category_scores)


class TestGenerateSuggestionsReport:

    def test_generates_markdown_with_suggestions(self, tmp_path):
        from update_stars import generate_suggestions_report

        def _mock_suggest(repos):
            return [
                _make_result(10000, "user/repo1", "Python", "A great tool", [
                    ("🤖", "Agentic Dev Tools", 9),
                    ("💻", "Dev Tools", 5),
                ]),
                _make_result(5000, "user/repo2", "Go", "CLI helper", [
                    ("⌨️", "Terminal CLI", 7),
                ]),
            ]

        fp = tmp_path / "suggestions.md"
        repos = [
            (10000, "user/repo1", "Python", "A great tool"),
            (5000, "user/repo2", "Go", "CLI helper"),
        ]
        with patch("update_stars.suggest_categories", side_effect=_mock_suggest):
            generate_suggestions_report(repos, str(fp))

        assert fp.exists()
        content = fp.read_text(encoding="utf-8")
        assert "# 🏷️ Categorization Suggestions" in content
        assert "2 repos analyzed" in content
        assert "## 🤖 Agentic Dev Tools" in content
        assert "## ⌨️ Terminal CLI" in content
        assert "user/repo1" in content
        assert "user/repo2" in content
        # Alt categories should appear
        assert "💻 Dev Tools (5)" in content

    def test_handles_empty_repos(self, tmp_path):
        from update_stars import generate_suggestions_report

        fp = tmp_path / "suggestions.md"
        with patch("update_stars.suggest_categories", return_value=[]):
            generate_suggestions_report([], str(fp))

        # Should not create file for empty repos
        assert not fp.exists()

    def test_no_category_repos_go_to_uncertain(self, tmp_path):
        from update_stars import generate_suggestions_report

        def _mock_suggest(repos):
            return [
                _make_result(3000, "user/mystery", "Brainfuck", "??", []),
            ]

        fp = tmp_path / "suggestions.md"
        repos = [(3000, "user/mystery", "Brainfuck", "??")]
        with patch("update_stars.suggest_categories", side_effect=_mock_suggest):
            generate_suggestions_report(repos, str(fp))

        content = fp.read_text(encoding="utf-8")
        assert "## ❓ Uncertain" in content
        assert "user/mystery" in content

    def test_groups_multiple_repos_by_top_category(self, tmp_path):
        from update_stars import generate_suggestions_report

        def _mock_suggest(repos):
            return [
                _make_result(8000, "user/ai1", "Python", "AI tool", [
                    ("🧠", "AI/LLM", 10),
                    ("💻", "Dev Tools", 3),
                ]),
                _make_result(6000, "user/ai2", "Python", "Another AI", [
                    ("🧠", "AI/LLM", 8),
                ]),
                _make_result(4000, "user/dev1", "Rust", "Dev tool", [
                    ("💻", "Dev Tools", 7),
                ]),
            ]

        fp = tmp_path / "suggestions.md"
        repos = [
            (8000, "user/ai1", "Python", "AI tool"),
            (6000, "user/ai2", "Python", "Another AI"),
            (4000, "user/dev1", "Rust", "Dev tool"),
        ]
        with patch("update_stars.suggest_categories", side_effect=_mock_suggest):
            generate_suggestions_report(repos, str(fp))

        content = fp.read_text(encoding="utf-8")
        assert "3 repos analyzed" in content
        # AI section should have 2 repos
        ai_idx = content.index("## 🧠 AI/LLM")
        dev_idx = content.index("## 💻 Dev Tools")
        assert ai_idx < dev_idx  # AI (2 repos) before Dev (1 repo)
        assert "user/ai1" in content
        assert "user/ai2" in content
        assert "user/dev1" in content

    def test_description_truncated_at_100_chars(self, tmp_path):
        from update_stars import generate_suggestions_report

        long_desc = "x" * 200
        def _mock_suggest(repos):
            return [
                _make_result(1000, "user/repo", "Python", long_desc, [
                    ("💻", "Dev Tools", 7),
                ]),
            ]

        fp = tmp_path / "suggestions.md"
        repos = [(1000, "user/repo", "Python", long_desc)]
        with patch("update_stars.suggest_categories", side_effect=_mock_suggest):
            generate_suggestions_report(repos, str(fp))

        content = fp.read_text(encoding="utf-8")
        # The description in the markdown should be truncated
        assert long_desc[:100] in content
        assert long_desc[:101] not in content  # 101st char not present

    def test_pipe_chars_replaced_in_description(self, tmp_path):
        from update_stars import generate_suggestions_report

        def _mock_suggest(repos):
            return [
                _make_result(1000, "user/repo", "Python", "a | b | c", [
                    ("💻", "Dev Tools", 7),
                ]),
            ]

        fp = tmp_path / "suggestions.md"
        repos = [(1000, "user/repo", "Python", "a | b | c")]
        with patch("update_stars.suggest_categories", side_effect=_mock_suggest):
            generate_suggestions_report(repos, str(fp))

        content = fp.read_text(encoding="utf-8")
        assert "a / b / c" in content
        assert "a | b | c" not in content

    def test_footer_present(self, tmp_path):
        from update_stars import generate_suggestions_report

        def _mock_suggest(repos):
            return [
                _make_result(1000, "user/repo", "Python", "test", [
                    ("💻", "Dev Tools", 7),
                ]),
            ]

        fp = tmp_path / "suggestions.md"
        repos = [(1000, "user/repo", "Python", "test")]
        with patch("update_stars.suggest_categories", side_effect=_mock_suggest):
            generate_suggestions_report(repos, str(fp))

        content = fp.read_text(encoding="utf-8")
        assert "Generated by `scripts/update_stars.py`" in content
