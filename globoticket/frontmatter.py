from pathlib import Path


def find_frontmatter_file(product_code: str, frontmatter_dir: Path) -> Path:
    """Find a file named `product_code`.yml in frontmatter_dir
    and its subdirectories.

    Raises FileNotFoundError if no file is found for this product_code."""

    # Please implement this function using Pathlib
