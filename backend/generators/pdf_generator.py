"""PDF generation from CV data."""

from typing import Any

from weasyprint import HTML  # type: ignore


def generate_pdf(
    cv_data: dict[str, Any], output_path: str, language: str = "en"
) -> None:
    """Generate PDF from CV data.

    Args:
        cv_data: Parsed CV data
        output_path: Path to save PDF
        language: Language code
    """
    # Create minimal HTML for PDF
    html_content = create_pdf_html(cv_data, language)

    # Generate PDF using WeasyPrint
    HTML(string=html_content).write_pdf(output_path)  # type: ignore


def create_pdf_html(cv_data: dict[str, Any], language: str) -> str:
    """Create HTML suitable for PDF generation.

    Args:
        cv_data: CV data (dict)
        language: Language code

    Returns:
        HTML string
    """
    personal = cv_data["personal"]
    name = personal["name"] or "CV"
    email = personal["email"] or ""
    phone = personal["phone"] or ""
    location = personal["location"] or ""
    birth_date = personal.get("birth_date")
    birth_date_str = str(birth_date) if birth_date else ""

    html = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

        body {{
            font-family: 'Inter', 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            color: #1a1a1a;
            margin: 0;
            padding: 50px;
            max-width: 210mm;
            background: #ffffff;
        }}

        .header {{
            text-align: center;
            margin-bottom: 40px;
            padding-bottom: 20px;
            border-bottom: 3px solid #2563eb;
        }}

        h1 {{
            color: #1e293b;
            margin: 0 0 8px 0;
            font-size: 32px;
            font-weight: 700;
            letter-spacing: -0.5px;
        }}

        .contact {{
            color: #64748b;
            font-size: 14px;
            font-weight: 500;
            margin-top: 8px;
        }}

        .contact p {{
            margin: 0;
            display: flex;
            justify-content: center;
            gap: 20px;
            flex-wrap: wrap;
        }}

        h2 {{
            color: #0f172a;
            font-size: 18px;
            font-weight: 600;
            margin: 35px 0 15px 0;
            text-transform: uppercase;
            letter-spacing: 1px;
            border-bottom: 2px solid #e2e8f0;
            padding-bottom: 8px;
        }}

        .entry {{
            margin-bottom: 20px;
            page-break-inside: avoid;
        }}

        .entry-header {{
            font-weight: 600;
            font-size: 16px;
            color: #1e293b;
            margin-bottom: 4px;
        }}

        .entry-subheader {{
            font-weight: 500;
            font-size: 14px;
            color: #2563eb;
            margin-bottom: 6px;
        }}

        .entry-meta {{
            color: #64748b;
            font-size: 13px;
            font-weight: 500;
            margin-bottom: 8px;
        }}

        .entry-description {{
            font-size: 14px;
            line-height: 1.6;
            color: #374151;
            margin: 0;
        }}

        .skills {{
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 20px;
            margin-top: 15px;
        }}

        .skill-category {{
            font-weight: 600;
            font-size: 14px;
            color: #1e293b;
            margin-bottom: 8px;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }}

        .skill-items {{
            font-size: 13px;
            color: #64748b;
            line-height: 1.5;
        }}

        .technologies {{
            background: #f1f5f9;
            padding: 8px 12px;
            border-radius: 6px;
            margin-top: 8px;
            display: inline-block;
        }}

        .technologies span {{
            background: #2563eb;
            color: white;
            padding: 2px 8px;
            border-radius: 12px;
            font-size: 11px;
            font-weight: 500;
            margin-right: 6px;
            margin-bottom: 4px;
            display: inline-block;
        }}

        a {{
            color: #2563eb;
            text-decoration: none;
        }}

        a:hover {{
            text-decoration: underline;
        }}

        @page {{
            margin: 25mm 20mm;
            size: A4;
        }}
    </style>
</head>
<body>
    <div class="header">
        <h1>{name}</h1>
        <div class="contact">
            <p>
                {f'<span>{email}</span>' if email else ''}
                {f'<span>{phone}</span>' if phone else ''}
                {f'<span>{location}</span>' if location else ''}
                {f'<span>{birth_date_str}</span>' if birth_date_str else ''}
            </p>
        </div>
    </div>

    <h2>{cv_data['translations'][language]['summary']}</h2>
    <p>{cv_data.get('summary', '')}</p>

    <h2>{cv_data['translations'][language]['experience']}</h2>
"""

    for exp in cv_data.get("experience", []):
        location_str = exp.get("location", "")
        location_part = f" | {location_str}" if location_str else ""
        meta = f"{exp['period']}{location_part}"
        html += f"""
    <div class="entry">
        <div class="entry-header">{exp['title']}</div>
        <div class="entry-subheader">{exp['company']}</div>
        <div class="entry-meta">
            {meta}
        </div>
        <div class="entry-description">{exp['description']}</div>
    </div>
"""

    html += f"""
    <h2>{cv_data['translations'][language]['education']}</h2>
"""

    for edu in cv_data.get("education", []):
        html += f"""
    <div class="entry">
        <div class="entry-header">{edu['degree']}</div>
        <div class="entry-subheader">{edu.get('school', '')}</div>
        <div class="entry-meta">{edu.get('graduation_year', '')}</div>
    </div>
"""

    html += f"""
    <h2>{cv_data['translations'][language]['skills']}</h2>
    <div class="skills">
"""

    for skill in cv_data.get("skills", []):
        html += f"""
        <div>
            <div class="skill-category">{skill['category']}</div>
            <div class="skill-items">{', '.join(skill['items'])}</div>
        </div>
"""

    html += """
    </div>
"""

    if cv_data.get("projects"):
        html += f"""
    <h2>{cv_data['translations'][language]['projects']}</h2>
"""
        for proj in cv_data.get("projects", []):
            html += f"""
    <div class="entry">
        <div class="entry-header">{proj['title']}</div>
        <div class="entry-description">{proj['description']}</div>
"""
            if proj.get("technologies"):
                html += f"""
        <div class="entry-meta">Technologies: {', '.join(proj['technologies'])}
        </div>
"""
            if proj.get("url"):
                html += f"""
        <div class="entry-meta"><a href="{proj['url']}">{proj['url']}</a></div>
"""
            html += """
    </div>
"""

    if cv_data.get("certifications"):
        html += f"""
    <h2>{cv_data['translations'][language]['certifications']}</h2>
"""
        for cert in cv_data.get("certifications", []):
            html += f"""
    <div class="entry">
        <div class="entry-header">{cert['title']}</div>
        <div class="entry-subheader">{cert.get('issuer', '')}</div>
        <div class="entry-meta">{cert.get('issued_date', '')}</div>
    </div>
"""

    html += """
</body>
</html>"""

    return html
