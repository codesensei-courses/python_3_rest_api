from pathlib import Path

import pytest

from globoticket.frontmatter import find_frontmatter_file

# The actual path where the frontmatter is located
FM_PATH = Path(__file__).parent / "product_info"


def test_find_file_toplevel():
    """Locate a yaml file at toplevel directory"""
    assert find_frontmatter_file("111222", FM_PATH) == FM_PATH / "111222.yml"


def test_find_file_subdirs():
    """Locate a yaml file in subdirectory"""
    assert find_frontmatter_file("123456", FM_PATH) == FM_PATH / "hiphop" / "123456.yml"
    assert find_frontmatter_file("654321", FM_PATH) == FM_PATH / "reggae" / "654321.yml"


def test_find_nosuchfile():
    """Raise correct exception when file does not exist"""
    with pytest.raises(FileNotFoundError):
        find_frontmatter_file("000000", FM_PATH)
