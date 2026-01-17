"""JSON generation from CV data."""

import json
from typing import Any


def generate_json(cv_data: dict[str, Any] | None) -> str:
    """Generate JSON from CV data.

    Args:
        cv_data: Parsed CV data (dict)

    Returns:
        JSON string with trailing newline
    """
    return json.dumps(cv_data, ensure_ascii=False, indent=2, default=str) + "\n"
