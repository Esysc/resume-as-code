"""YAML parser for CV data."""

from typing import Any

import yaml


def parse_cv_file(filepath: str) -> dict[str, Any]:
    """Parse CV YAML file.

    Args:
        filepath: Path to YAML file

    Returns:
        Parsed CV data dictionary
    """
    with open(filepath, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)
    return data or {}
