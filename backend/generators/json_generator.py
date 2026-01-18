"""JSON generation from CV data.

Includes helpers to produce sanitized public JSON by removing PII
and obfuscating email with base64 encoding.
"""

import base64
import json
from typing import Any, Dict

PII_FIELDS = {"phone", "birth_date"}


def _sanitize_public(data: Dict[str, Any]) -> Dict[str, Any]:
    """Return a sanitized copy of CV data for public use.

    Removes phone and birth_date from personal section.
    Base64-encodes email to make it less scrapable.
    """
    # Deep copy to avoid modifying original
    sanitized = dict(data)
    personal = dict(sanitized.get("personal", {}))

    # Remove PII fields
    for key in PII_FIELDS:
        personal.pop(key, None)

    # Obfuscate email if present: split@reverse->encode->reverse
    if "email" in personal:
        email = personal["email"]
        # Split at @
        user, domain = email.split("@")
        # Reverse each part
        user_rev = user[::-1]
        domain_rev = domain[::-1]
        # Base64 encode each reversed part
        user_encoded = base64.b64encode(user_rev.encode("utf-8")).decode("utf-8")
        domain_encoded = base64.b64encode(domain_rev.encode("utf-8")).decode("utf-8")
        # Reverse the encoded strings
        user_final = user_encoded[::-1]
        domain_final = domain_encoded[::-1]
        # Store as "reversedEncoded@reversedEncoded"
        personal["email"] = f"{user_final}@{domain_final}"

    sanitized["personal"] = personal
    return sanitized


def generate_json(cv_data: dict[str, Any] | None) -> str:
    """Generate JSON from CV data.

    Args:
        cv_data: Parsed CV data (dict)

    Returns:
        JSON string with trailing newline
    """
    return json.dumps(cv_data, ensure_ascii=False, indent=2, default=str) + "\n"


def generate_public_json(cv_data: dict[str, Any]) -> str:
    """Generate sanitized public JSON without PII and obfuscated email.

    Args:
        cv_data: Parsed and validated CV data (dict)

    Returns:
        Sanitized JSON string with trailing newline
    """
    sanitized = _sanitize_public(cv_data)
    return json.dumps(sanitized, ensure_ascii=False, indent=2, default=str) + "\n"
