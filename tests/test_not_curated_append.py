"""Tests for append_new_to_not_curated: appending uncategorized repos to NOT-CURATED.md."""
import pytest
from unittest.mock import patch


class TestAppendNewToNotCurated:
    """append_new_to_not_curated(stars_db, curated_repos, filepath)."""

    def test_all_repos_already_curated_returns_zero(self, tmp_path):
        """When every repo in stars_db is already in curated_repos, return 0 and don't write."""
        from update_stars import append_new_to_not_curated

        stars_db = {
            "user/a": (100, "Python", "A tool"),
            "user/b": (200, "Go", "B tool"),
        }
        curated = ["user/a", "user/b"]
        nc_file = tmp_path / "NOT-CURATED.md"

        result = append_new_to_not_curated(stars_db, curated, str(nc_file))

        assert result == 0
        assert not nc_file.exists()  # file never created since nothing to append

    def test_new_repos_appended_with_correct_format(self, tmp_path):
        """New repos not in curated_repos get appended with header, stars, and formatting."""
        from update_stars import append_new_to_not_curated

        stars_db = {
            "user/new-tool": (5000, "Rust", "A new tool for things"),
        }
        curated = []
        nc_file = tmp_path / "NOT-CURATED.md"

        with patch("update_stars.datetime") as mock_dt:
            mock_dt.now.return_value.strftime.return_value = "2026-07-16 12:00 UTC"
            result = append_new_to_not_curated(stars_db, curated, str(nc_file))

        assert result == 1
        content = nc_file.read_text(encoding="utf-8")

        assert "## 🆕 New Stars — 2026-07-16 12:00 UTC" in content
        assert "[user/new-tool](https://github.com/user/new-tool)" in content
        assert "⭐5000" in content
        assert "(Rust)" in content
        assert "A new tool for things" in content

    def test_repos_already_in_not_curated_file_are_excluded(self, tmp_path):
        """If NOT-CURATED.md already exists, repos listed there are excluded from new batch."""
        from update_stars import append_new_to_not_curated

        stars_db = {
            "user/already-there": (100, "JS", "Already listed"),
            "user/genuinely-new": (200, "TS", "Truly new"),
        }
        curated = []
        nc_file = tmp_path / "NOT-CURATED.md"
        # Pre-populate NOT-CURATED with one repo
        nc_file.write_text(
            "# Not Curated\n\n"
            "## Old Batch\n\n"
            "- [user/already-there](https://github.com/user/already-there) — ⭐100 (JS) Already listed\n"
        )

        with patch("update_stars.datetime") as mock_dt:
            mock_dt.now.return_value.strftime.return_value = "2026-07-16 12:00 UTC"
            result = append_new_to_not_curated(stars_db, curated, str(nc_file))

        assert result == 1
        content = nc_file.read_text(encoding="utf-8")
        # Original NC file content is preserved (append mode)
        assert "user/already-there" in content
        assert "user/genuinely-new" in content
        # The already-there repo shouldn't appear in the NEW batch
        new_batch = content.split("## 🆕 New Stars —")[1]
        assert "user/already-there" not in new_batch

    def test_description_truncated_at_120_chars(self, tmp_path):
        """Long descriptions are truncated at 120 characters."""
        from update_stars import append_new_to_not_curated

        long_desc = "A" * 200
        stars_db = {
            "user/big-desc": (50, "Python", long_desc),
        }
        curated = []
        nc_file = tmp_path / "NOT-CURATED.md"

        with patch("update_stars.datetime") as mock_dt:
            mock_dt.now.return_value.strftime.return_value = "2026-07-16 12:00 UTC"
            append_new_to_not_curated(stars_db, curated, str(nc_file))

        content = nc_file.read_text(encoding="utf-8")
        # Description should be exactly 120 chars (not 200)
        assert "A" * 120 in content
        assert "A" * 121 not in content

    def test_pipe_in_description_replaced_with_slash(self, tmp_path):
        """Pipe characters in descriptions are replaced with '/'."""
        from update_stars import append_new_to_not_curated

        stars_db = {
            "user/pipe-desc": (50, "Python", "Uses a|b|c pipes"),
        }
        curated = []
        nc_file = tmp_path / "NOT-CURATED.md"

        with patch("update_stars.datetime") as mock_dt:
            mock_dt.now.return_value.strftime.return_value = "2026-07-16 12:00 UTC"
            append_new_to_not_curated(stars_db, curated, str(nc_file))

        content = nc_file.read_text(encoding="utf-8")
        assert "Uses a/b/c pipes" in content
        assert "Uses a|b|c pipes" not in content

    def test_none_desc_and_lang_use_fallbacks(self, tmp_path):
        """None description becomes empty string, None lang becomes '-'."""
        from update_stars import append_new_to_not_curated

        stars_db = {
            "user/no-meta": (50, None, None),
        }
        curated = []
        nc_file = tmp_path / "NOT-CURATED.md"

        with patch("update_stars.datetime") as mock_dt:
            mock_dt.now.return_value.strftime.return_value = "2026-07-16 12:00 UTC"
            append_new_to_not_curated(stars_db, curated, str(nc_file))

        content = nc_file.read_text(encoding="utf-8")
        assert "(-)" in content
        assert "(None)" not in content

    def test_repos_sorted_by_stars_descending(self, tmp_path):
        """New repos are sorted by star count descending in the output."""
        from update_stars import append_new_to_not_curated

        stars_db = {
            "user/small": (10, "JS", "Small"),
            "user/big": (9999, "Rust", "Big"),
            "user/medium": (500, "Go", "Medium"),
        }
        curated = []
        nc_file = tmp_path / "NOT-CURATED.md"

        with patch("update_stars.datetime") as mock_dt:
            mock_dt.now.return_value.strftime.return_value = "2026-07-16 12:00 UTC"
            append_new_to_not_curated(stars_db, curated, str(nc_file))

        content = nc_file.read_text(encoding="utf-8")
        # Find positions in output
        pos_big = content.index("user/big")
        pos_medium = content.index("user/medium")
        pos_small = content.index("user/small")

        assert pos_big < pos_medium < pos_small  # descending stars

    def test_empty_stars_db_returns_zero(self, tmp_path):
        """Empty stars_db returns 0 without writing anything."""
        from update_stars import append_new_to_not_curated

        stars_db = {}
        curated = []
        nc_file = tmp_path / "NOT-CURATED.md"

        result = append_new_to_not_curated(stars_db, curated, str(nc_file))

        assert result == 0
        assert not nc_file.exists()

    def test_newline_in_description_replaced_with_space(self, tmp_path):
        """Newlines in descriptions are replaced with spaces."""
        from update_stars import append_new_to_not_curated

        stars_db = {
            "user/multiline": (50, "Python", "Line 1\nLine 2\nLine 3"),
        }
        curated = []
        nc_file = tmp_path / "NOT-CURATED.md"

        with patch("update_stars.datetime") as mock_dt:
            mock_dt.now.return_value.strftime.return_value = "2026-07-16 12:00 UTC"
            append_new_to_not_curated(stars_db, curated, str(nc_file))

        content = nc_file.read_text(encoding="utf-8")
        assert "Line 1 Line 2 Line 3" in content
        assert "Line 1\nLine 2" not in content

    def test_repos_with_equal_stars_preserve_dict_order(self, tmp_path):
        """Equal star counts: Python's stable sort preserves dict insertion order."""
        from update_stars import append_new_to_not_curated

        stars_db = {
            "user/first": (100, "A", ""),
            "user/second": (100, "B", ""),
        }
        curated = []
        nc_file = tmp_path / "NOT-CURATED.md"

        with patch("update_stars.datetime") as mock_dt:
            mock_dt.now.return_value.strftime.return_value = "2026-07-16 12:00 UTC"
            append_new_to_not_curated(stars_db, curated, str(nc_file))

        content = nc_file.read_text(encoding="utf-8")
        pos_first = content.index("user/first")
        pos_second = content.index("user/second")
        assert pos_first < pos_second  # stable sort preserves insertion order

    def test_not_curated_file_does_not_exist_yet(self, tmp_path):
        """When NOT-CURATED.md doesn't exist, the function still works (creates it)."""
        from update_stars import append_new_to_not_curated

        stars_db = {
            "user/first-ever": (100, "Python", "First entry"),
        }
        curated = []
        nc_file = tmp_path / "NOT-CURATED.md"
        # File does NOT exist yet

        with patch("update_stars.datetime") as mock_dt:
            mock_dt.now.return_value.strftime.return_value = "2026-07-16 12:00 UTC"
            result = append_new_to_not_curated(stars_db, curated, str(nc_file))

        assert result == 1
        assert nc_file.exists()
        content = nc_file.read_text(encoding="utf-8")
        assert "user/first-ever" in content

    def test_case_insensitive_dedup_prevents_duplicates(self, tmp_path):
        """GitHub repo renames (FastApps vs fastapps) are caught by case-insensitive check."""
        from update_stars import append_new_to_not_curated, extract_repos_from_file

        # Simulate: NOT-CURATED has "user/fastapps" (old casing)
        # DB has "user/FastApps" (new casing after rename)
        stars_db = {
            "user/FastApps": (100, "Python", "Renamed repo"),
        }
        curated = []
        nc_file = tmp_path / "NOT-CURATED.md"
        nc_file.write_text(
            "# Not Curated\n\n"
            "## Old Batch\n\n"
            "- [user/fastapps](https://github.com/user/fastapps) — ⭐100 (Python) Old casing\n"
        )

        # Case-sensitive check (OLD BUG): would return 1, creating a duplicate
        # Case-insensitive check (FIX): should return 0
        result = append_new_to_not_curated(stars_db, curated, str(nc_file))

        # Verify: old lowercased entry excluded the new-cased repo → 0 appended
        assert result == 0

        # Double-check: extract_repos_from_file still returns the old casing
        repos = extract_repos_from_file(str(nc_file))
        assert "user/fastapps" in repos  # extracted with original casing

        # The FIX: comparing .lower() versions catches the duplicate
        nc_lower = set(r.lower() for r in repos)
        assert "user/fastapps" in nc_lower  # old casing, lowered
        assert "user/fastapps" == "user/FastApps".lower()
