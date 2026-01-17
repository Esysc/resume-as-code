#!/usr/bin/env python3
"""Validate CV YAML files against schema."""

import sys
from pathlib import Path
from typing import Any

from backend.parsers.schema import validate_cv
from backend.parsers.yaml_parser import parse_cv_with_base


def main():
    """Validate all CV YAML files."""
    script_dir = Path(__file__).parent
    cv_data_dir = script_dir.parent / "cv-data"
    languages = ["en", "fr", "it"]

    errors: list[str] = []

    for lang in languages:
        cv_file = cv_data_dir / f"cv_{lang}.yml"
        if not cv_file.exists():
            errors.append(f"CV file {cv_file} does not exist")
            continue

        try:
            # Parse YAML (merges with English base for non-English files)
            cv_data: dict[str, Any] = parse_cv_with_base(str(cv_file))

            # Validate schema
            validate_cv(cv_data)

            print(f"✓ {lang.upper()}: Valid")

        except Exception as e:
            errors.append(f"✗ {lang.upper()}: {e}")

    if errors:
        print("\nValidation errors:")
        for error in errors:
            print(f"  {error}")
        sys.exit(1)

    print("\n✅ All CV files are valid!")


if __name__ == "__main__":
    main()
