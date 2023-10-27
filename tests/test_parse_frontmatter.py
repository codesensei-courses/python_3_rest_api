import pytest

from globoticket.frontmatter import InvalidFrontmatterError, parse_frontmatter


def test_parse_frontmatter():
    """Parse a frontmatter file."""
    fm = parse_frontmatter(
        """---
name: Live at Folsom Prison
artist: Johnny Cash
published: false
---
Sold out"""
    )
    assert fm == {
        "content": "Sold out",
        "name": "Live at Folsom Prison",
        "artist": "Johnny Cash",
        "published": False,
    }


def test_parse_empty():
    """An empty file causes an error. So do files with only dashes in them."""
    for s in ["", "----", "---\n---"]:
        with pytest.raises(InvalidFrontmatterError):
            parse_frontmatter(s)


def test_parse_content_only():
    """A file without YAML raises an error"""
    with pytest.raises(InvalidFrontmatterError):
        parse_frontmatter(
            """---
---
Test content"""
        )


def test_parse_yaml_only():
    """Parse a file with YAML but empty content."""
    fm = parse_frontmatter(
        """---
name: Live at Folsom Prison
artist: Johnny Cash
published: false
---
"""
    )
    assert fm == {
        "content": "",
        "name": "Live at Folsom Prison",
        "artist": "Johnny Cash",
        "published": False,
    }


def test_parse_yaml_invalid():
    """Invalid YAML is not allowed."""
    with pytest.raises(InvalidFrontmatterError):
        parse_frontmatter(
            """---
    - name: test
    - artist: testartist
    - published: true
    ---
    Test content!"""
        )
