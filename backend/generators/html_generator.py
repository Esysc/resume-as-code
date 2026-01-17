"""HTML generation from CV data."""

from pathlib import Path
from typing import Any

from jinja2 import Template


def generate_html(cv_data: dict[str, str], language: str = "en") -> str:
    """Generate HTML from CV data.

    Args:
        cv_data: Parsed CV data
        language: Language code (en, fr, it)

    Returns:
        HTML string
    """
    template_path = Path(__file__).parent.parent / "templates" / "cv.html"

    if not template_path.exists():
        # Fallback: generate minimal HTML
        return generate_minimal_html(cv_data)

    with open(template_path, "r", encoding="utf-8") as f:
        template_str = f.read()

    template = Template(template_str)
    html = template.render(cv=cv_data, lang=language)

    return html


def generate_minimal_html(cv_data: dict[str, Any]) -> str:
    """Generate minimal HTML when template not found.

    Args:
        cv_data: Parsed CV data
        language: Language code (en, fr, it)

    Returns:
        HTML string
    """
    name = cv_data.get("personal", {}).get("name", "CV")

    html = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{name} - CV</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            line-height: 1.6;
            max-width: 900px;
            margin: 0 auto;
            padding: 20px;
            color: #333;
        }}
        h1 {{ color: #2563eb; }}
        h2 {{ color: #1e40af; margin-top: 30px; }}
        .contact {{ color: #666; font-size: 0.9em; }}
    </style>
</head>
<body>
    <h1>{name}</h1>
    <div class="contact">
        <p>{cv_data.get("personal", {}).get("email")} | {cv_data.get("personal", {}).get("phone")}</p>
    </div>

    <h2>Summary</h2>
    <p>{cv_data.get("summary", "")}</p>

    <h2>Experience</h2>
    {
        "".join([
            f"""
                <h3>{exp.get('title')} at {exp.get('company')}</h3>
                <p>{exp.get('description')}</p>
            """
            for exp in cv_data.get("experience", [])])}

    <h2>Education</h2>
    {
        "".join([
            f"<p><strong>{edu.get('degree')}</strong></p>"
            for edu in cv_data.get("education", [])
        ])
    }
</body>
</html>"""

    return html
