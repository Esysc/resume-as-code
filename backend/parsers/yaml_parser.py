"""YAML parser for CV data."""

from pathlib import Path
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


def deep_merge(base: dict[str, Any], override: dict[str, Any]) -> dict[str, Any]:
    """Deep merge override into base dict.

    Lists are merged by matching 'id' field if present.

    Args:
        base: Base dictionary
        override: Override dictionary

    Returns:
        Merged dictionary
    """
    result = base.copy()

    for key, value in override.items():
        if key in result:
            if isinstance(result[key], dict) and isinstance(value, dict):
                result[key] = deep_merge(result[key], value)
            elif isinstance(result[key], list) and isinstance(value, list):
                # Merge lists by matching 'id' field
                result[key] = merge_lists_by_id(result[key], value)
            else:
                result[key] = value
        else:
            result[key] = value

    return result


def merge_lists_by_id(base_list: list[Any], override_list: list[Any]) -> list[Any]:
    """Merge two lists by matching 'id' field.

    Args:
        base_list: Base list
        override_list: Override list

    Returns:
        Merged list
    """
    # Create lookup by id for base items
    base_by_id = {}
    for item in base_list:
        if isinstance(item, dict) and "id" in item:
            base_by_id[item["id"]] = item

    result = []
    for item in base_list:
        if isinstance(item, dict) and "id" in item:
            item_id = item["id"]
            # Find matching override
            override_item = next(
                (o for o in override_list if isinstance(o, dict) and o.get("id") == item_id),
                None,
            )
            if override_item:
                result.append(deep_merge(item, override_item))
            else:
                result.append(item)
        else:
            result.append(item)

    return result


def parse_cv_with_base(filepath: str, base_lang: str = "en") -> dict[str, Any]:
    """Parse CV file with English as base and merge overrides.

    Args:
        filepath: Path to language-specific CV file
        base_lang: Base language code (default: en)

    Returns:
        Merged CV data dictionary
    """
    path = Path(filepath)
    lang = path.stem.replace("cv_", "")

    # If it's the base language, just return it
    if lang == base_lang:
        return parse_cv_file(filepath)

    # Load base (English) file
    base_file = path.parent / f"cv_{base_lang}.yml"
    base_data = parse_cv_file(str(base_file))

    # Load language override
    override_data = parse_cv_file(filepath)

    # Merge
    return deep_merge(base_data, override_data)
