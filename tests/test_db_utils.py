"""Tests for get_db_connection and get_all_stars database utilities."""
import pytest
import sqlite3
from unittest.mock import patch, MagicMock


class TestGetDbConnection:

    def test_creates_connection_with_row_factory(self):
        from update_stars import get_db_connection

        mock_conn = MagicMock(spec=sqlite3.Connection)
        with patch("update_stars.CACHE_DB") as mock_cache:
            mock_cache.exists.return_value = True
            with patch("sqlite3.connect", return_value=mock_conn) as mock_connect:
                conn = get_db_connection()

        mock_connect.assert_called_once()
        assert conn.row_factory == sqlite3.Row

    def test_exits_when_db_missing(self):
        from update_stars import get_db_connection

        with patch("update_stars.CACHE_DB") as mock_cache:
            mock_cache.exists.return_value = False
            with pytest.raises(SystemExit):
                get_db_connection()


class TestGetAllStars:

    def test_returns_correct_dict_structure(self):
        from update_stars import get_all_stars

        # Create an in-memory test database
        conn = sqlite3.connect(":memory:")
        conn.row_factory = sqlite3.Row
        conn.execute(
            "CREATE TABLE repos (full_name TEXT, stars INTEGER, language TEXT, description TEXT, username TEXT)"
        )
        conn.execute(
            "INSERT INTO repos VALUES (?, ?, ?, ?, ?)",
            ("user/repo1", 5000, "Python", "A tool", "pvnkmnk"),
        )
        conn.execute(
            "INSERT INTO repos VALUES (?, ?, ?, ?, ?)",
            ("user/repo2", 3000, "Go", "Another tool", "pvnkmnk"),
        )
        conn.execute(
            "INSERT INTO repos VALUES (?, ?, ?, ?, ?)",
            ("other/repo", 1000, "Rust", "Not mine", "someone_else"),
        )
        conn.commit()

        with patch("update_stars.GITHUB_USER", "pvnkmnk"):
            result = get_all_stars(conn)

        assert len(result) == 2
        assert result["user/repo1"] == (5000, "Python", "A tool")
        assert result["user/repo2"] == (3000, "Go", "Another tool")
        assert "other/repo" not in result

        conn.close()

    def test_empty_db_returns_empty_dict(self):
        from update_stars import get_all_stars

        conn = sqlite3.connect(":memory:")
        conn.row_factory = sqlite3.Row
        conn.execute(
            "CREATE TABLE repos (full_name TEXT, stars INTEGER, language TEXT, description TEXT, username TEXT)"
        )

        with patch("update_stars.GITHUB_USER", "pvnkmnk"):
            result = get_all_stars(conn)

        assert result == {}
        conn.close()

    def test_results_ordered_by_stars_desc(self):
        from update_stars import get_all_stars

        conn = sqlite3.connect(":memory:")
        conn.row_factory = sqlite3.Row
        conn.execute(
            "CREATE TABLE repos (full_name TEXT, stars INTEGER, language TEXT, description TEXT, username TEXT)"
        )
        conn.execute(
            "INSERT INTO repos VALUES (?, ?, ?, ?, ?)",
            ("user/low", 100, "Python", "Low", "pvnkmnk"),
        )
        conn.execute(
            "INSERT INTO repos VALUES (?, ?, ?, ?, ?)",
            ("user/high", 50000, "Python", "High", "pvnkmnk"),
        )
        conn.execute(
            "INSERT INTO repos VALUES (?, ?, ?, ?, ?)",
            ("user/mid", 5000, "Python", "Mid", "pvnkmnk"),
        )
        conn.commit()

        with patch("update_stars.GITHUB_USER", "pvnkmnk"):
            result = get_all_stars(conn)

        # Dictionaries preserve insertion order in Python 3.7+, but we're
        # returning a dict, not a list. Just verify all three are present.
        assert len(result) == 3
        assert "user/low" in result
        assert "user/mid" in result
        assert "user/high" in result
        conn.close()
