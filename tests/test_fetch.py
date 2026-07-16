"""Tests for fetch_stars(): gh api --paginate → SQLite database."""
import sqlite3
import sys
import subprocess
from pathlib import Path
from unittest.mock import patch, MagicMock

import pytest

# Ensure the scripts directory is on sys.path for imports
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

from update_stars import fetch_stars, GITHUB_USER


# ── Sample TSV fixtures ────────────────────────────────────────

@pytest.fixture
def tsv_happy_path():
    """Known-good TSV from gh api with realistic repo data."""
    return (
        "microsoft/vscode\t185000\tTypeScript\tVisual Studio Code editor\t"
        "https://github.com/microsoft/vscode\t2020-01-01T00:00:00Z\t2026-07-01T00:00:00Z\n"
        "torvalds/linux\t200000\tC\tLinux kernel source tree\t"
        "https://github.com/torvalds/linux\t2015-01-01T00:00:00Z\t2026-07-01T00:00:00Z\n"
        "none/null-repo\t500\t-\t\t"
        "https://github.com/none/null-repo\t2018-01-01T00:00:00Z\t2026-07-01T00:00:00Z\n"
    )


@pytest.fixture
def tsv_with_malformed():
    """TSV with a line that has fewer than 7 fields (should be skipped)."""
    return (
        "ok/repo\t100\tRust\tA good repo\t"
        "https://github.com/ok/repo\t2020-01-01T00:00:00Z\t2026-07-01T00:00:00Z\n"
        "bad/repo\t50\tPython\tIncomplete line\n"
        "another/ok\t200\tGo\tAnother good one\t"
        "https://github.com/another/ok\t2020-01-01T00:00:00Z\t2026-07-01T00:00:00Z\n"
    )


@pytest.fixture
def tsv_invalid_stars():
    """TSV with a non-numeric stars value (should default to 0)."""
    return (
        "nan/repo\tnot_a_number\tPython\tStars is not a number\t"
        "https://github.com/nan/repo\t2020-01-01T00:00:00Z\t2026-07-01T00:00:00Z\n"
        "real/repo\t999\tPython\tReal stars here\t"
        "https://github.com/real/repo\t2020-01-01T00:00:00Z\t2026-07-01T00:00:00Z\n"
    )


# ── Test helper ────────────────────────────────────────────────

def _db_rows(db_path):
    """Return all rows from the repos table as list of tuples."""
    conn = sqlite3.connect(str(db_path))
    rows = conn.execute("SELECT * FROM repos ORDER BY stars DESC").fetchall()
    conn.close()
    return rows


def _db_schema(db_path):
    """Return column names from the repos table."""
    conn = sqlite3.connect(str(db_path))
    cursor = conn.execute("PRAGMA table_info(repos)")
    cols = [(r[1], r[2]) for r in cursor.fetchall()]  # (name, type)
    conn.close()
    return cols


# ── Tests ──────────────────────────────────────────────────────

class TestFetchStarsHappyPath:
    """Happy path: valid TSV → correct SQLite database."""

    def test_db_created_with_correct_schema(self, tmp_path, tsv_happy_path):
        db_path = tmp_path / "stars.db"
        mock_result = MagicMock(returncode=0, stdout=tsv_happy_path, stderr="")

        with patch("update_stars.CACHE_DB", db_path):
            with patch("subprocess.run", return_value=mock_result):
                fetch_stars()

        assert db_path.exists()
        cols = _db_schema(db_path)
        col_names = [c[0] for c in cols]
        assert col_names == ["full_name", "stars", "language", "description",
                             "html_url", "created_at", "updated_at", "username"]

    def test_correct_row_count(self, tmp_path, tsv_happy_path):
        db_path = tmp_path / "stars.db"
        mock_result = MagicMock(returncode=0, stdout=tsv_happy_path, stderr="")

        with patch("update_stars.CACHE_DB", db_path):
            with patch("subprocess.run", return_value=mock_result):
                fetch_stars()

        rows = _db_rows(db_path)
        assert len(rows) == 3

    def test_username_column_is_set(self, tmp_path, tsv_happy_path):
        db_path = tmp_path / "stars.db"
        mock_result = MagicMock(returncode=0, stdout=tsv_happy_path, stderr="")

        with patch("update_stars.CACHE_DB", db_path):
            with patch("subprocess.run", return_value=mock_result):
                fetch_stars()

        conn = sqlite3.connect(str(db_path))
        usernames = [r[0] for r in conn.execute("SELECT username FROM repos").fetchall()]
        conn.close()
        assert all(u == GITHUB_USER for u in usernames)


class TestFetchStarsNullHandling:
    """Null language → '-', null description → ''."""

    def test_null_language_becomes_dash(self, tmp_path, tsv_happy_path):
        db_path = tmp_path / "stars.db"
        mock_result = MagicMock(returncode=0, stdout=tsv_happy_path, stderr="")

        with patch("update_stars.CACHE_DB", db_path):
            with patch("subprocess.run", return_value=mock_result):
                fetch_stars()

        conn = sqlite3.connect(str(db_path))
        lang = conn.execute(
            "SELECT language FROM repos WHERE full_name=?", ("none/null-repo",)
        ).fetchone()[0]
        conn.close()
        assert lang == "-"

    def test_null_description_becomes_empty_string(self, tmp_path, tsv_happy_path):
        db_path = tmp_path / "stars.db"
        mock_result = MagicMock(returncode=0, stdout=tsv_happy_path, stderr="")

        with patch("update_stars.CACHE_DB", db_path):
            with patch("subprocess.run", return_value=mock_result):
                fetch_stars()

        conn = sqlite3.connect(str(db_path))
        desc = conn.execute(
            "SELECT description FROM repos WHERE full_name=?", ("none/null-repo",)
        ).fetchone()[0]
        conn.close()
        assert desc == ""

    def test_stars_are_integers(self, tmp_path, tsv_happy_path):
        db_path = tmp_path / "stars.db"
        mock_result = MagicMock(returncode=0, stdout=tsv_happy_path, stderr="")

        with patch("update_stars.CACHE_DB", db_path):
            with patch("subprocess.run", return_value=mock_result):
                fetch_stars()

        conn = sqlite3.connect(str(db_path))
        stars = [r[1] for r in conn.execute("SELECT * FROM repos ORDER BY stars DESC").fetchall()]
        conn.close()
        assert stars == [200000, 185000, 500]


class TestFetchStarsEdgeCases:
    """Malformed lines, invalid stars, empty results, gh api failure."""

    def test_malformed_line_skipped(self, tmp_path, tsv_with_malformed):
        db_path = tmp_path / "stars.db"
        mock_result = MagicMock(returncode=0, stdout=tsv_with_malformed, stderr="")

        with patch("update_stars.CACHE_DB", db_path):
            with patch("subprocess.run", return_value=mock_result):
                fetch_stars()

        rows = _db_rows(db_path)
        assert len(rows) == 2  # malformed line skipped
        names = [r[0] for r in rows]
        assert "ok/repo" in names
        assert "another/ok" in names
        assert "bad/repo" not in names

    def test_invalid_stars_defaults_to_zero(self, tmp_path, tsv_invalid_stars):
        db_path = tmp_path / "stars.db"
        mock_result = MagicMock(returncode=0, stdout=tsv_invalid_stars, stderr="")

        with patch("update_stars.CACHE_DB", db_path):
            with patch("subprocess.run", return_value=mock_result):
                fetch_stars()

        conn = sqlite3.connect(str(db_path))
        stars = conn.execute(
            "SELECT stars FROM repos WHERE full_name=?", ("nan/repo",)
        ).fetchone()[0]
        conn.close()
        assert stars == 0

    def test_empty_stdout_exits(self, tmp_path):
        db_path = tmp_path / "stars.db"
        mock_result = MagicMock(returncode=0, stdout="\n\n", stderr="")

        with patch("update_stars.CACHE_DB", db_path):
            with patch("subprocess.run", return_value=mock_result):
                with pytest.raises(SystemExit) as exc_info:
                    fetch_stars()

        assert exc_info.value.code == 1

    def test_non_zero_exit_code_exits(self, tmp_path):
        db_path = tmp_path / "stars.db"
        mock_result = MagicMock(
            returncode=1,
            stdout="",
            stderr="gh: authentication required",
        )

        with patch("update_stars.CACHE_DB", db_path):
            with patch("subprocess.run", return_value=mock_result):
                with pytest.raises(SystemExit) as exc_info:
                    fetch_stars()

        assert exc_info.value.code == 1

    def test_gh_api_command_structure(self, tmp_path, tsv_happy_path):
        """Verify the actual gh api command arguments are correct."""
        db_path = tmp_path / "stars.db"
        mock_result = MagicMock(returncode=0, stdout=tsv_happy_path, stderr="")

        with patch("update_stars.CACHE_DB", db_path):
            with patch("subprocess.run") as mock_run:
                mock_run.return_value = mock_result
                fetch_stars()

        call_args = mock_run.call_args[0][0]
        assert call_args[0] == "gh"
        assert call_args[1] == "api"
        assert call_args[2] == "--paginate"
        assert f"/users/{GITHUB_USER}/starred" in call_args[3]
        assert call_args[4] == "--jq"
        assert call_args[5].endswith(" | @tsv")

    def test_database_replaces_on_second_fetch(self, tmp_path, tsv_happy_path):
        """Running fetch_stars twice should DROP TABLE and recreate (not duplicate)."""
        db_path = tmp_path / "stars.db"
        mock_result = MagicMock(returncode=0, stdout=tsv_happy_path, stderr="")

        with patch("update_stars.CACHE_DB", db_path):
            with patch("subprocess.run", return_value=mock_result):
                fetch_stars()
                # Modify stdout to return fewer repos on second call
                mock_result.stdout = (
                    "only/repo\t1\tShell\tLonely repo\t"
                    "https://github.com/only/repo\t2020-01-01T00:00:00Z\t2026-07-01T00:00:00Z\n"
                )
                fetch_stars()

        rows = _db_rows(db_path)
        assert len(rows) == 1
        assert rows[0][0] == "only/repo"
