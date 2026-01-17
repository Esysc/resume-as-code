"""
Main CV generation script.

Parses YAML CV data and generates HTML, JSON, and PDF outputs.
"""

from pathlib import Path

from backend.generators.html_generator import generate_html
from backend.generators.json_generator import generate_json
from backend.generators.pdf_generator import generate_pdf
from backend.parsers.schema import validate_cv
from backend.parsers.yaml_parser import parse_cv_file


def main():
    """Generate CV outputs from YAML sources."""

    # Paths
    cv_data_dir = Path(__file__).parent.parent / "cv-data"
    dist_dir = Path(__file__).parent.parent / "dist"
    dist_dir.mkdir(exist_ok=True)
    web_public_dir = Path(__file__).parent.parent / "web" / "public"
    web_public_dir.mkdir(exist_ok=True)

    # Load UI translations
    ui_translations_file = cv_data_dir / "ui_translations.yml"
    ui_translations = parse_cv_file(str(ui_translations_file))

    languages = ["en", "fr", "it"]

    print("🔄 Resume-as-Code Generator")
    print("=" * 50)

    for lang in languages:
        cv_file = cv_data_dir / f"cv_{lang}.yml"

        if not cv_file.exists():
            print(f"⚠️  Skipping {lang}: {cv_file} not found")
            continue

        print(f"\n📝 Processing: {lang.upper()}")

        # Parse YAML
        try:
            cv_data = parse_cv_file(str(cv_file))
            print("  ✓ Parsed YAML")
        except Exception as e:
            print(f"  ✗ Failed to parse: {e}")
            continue

        # Validate schema
        try:
            cv_data = validate_cv(cv_data)
            # Add UI translations
            cv_data = cv_data.model_dump()
            cv_data["translations"] = ui_translations
            print("  ✓ Validated schema")
        except Exception as e:
            print(f"  ✗ Validation failed: {e}")
            continue

        # Generate HTML
        try:
            html_content = generate_html(cv_data, lang)
            html_file = dist_dir / f"cv_{lang}.html"
            html_file.write_text(html_content)
            print(f"  ✓ Generated HTML → {html_file.name}")
        except Exception as e:
            print(f"  ✗ HTML generation failed: {e}")

        # Generate JSON
        try:
            json_content = generate_json(cv_data)
            json_file = dist_dir / f"cv_{lang}.json"
            json_file.write_text(json_content)
            # Copy to web/public for frontend
            web_json_file = web_public_dir / f"cv_{lang}.json"
            web_json_file.write_text(json_content)
            print(f"  ✓ Generated JSON → {json_file.name}")
        except Exception as e:
            print(f"  ✗ JSON generation failed: {e}")

        # Generate PDF
        try:
            pdf_file = dist_dir / f"cv_{lang}.pdf"
            generate_pdf(cv_data, str(pdf_file), lang)
            print(f"  ✓ Generated PDF → {pdf_file.name}")
        except Exception as e:
            print(f"  ✗ PDF generation failed: {e}")

    print("\n" + "=" * 50)
    print("✅ Generation complete!")
    print(f"📁 Outputs: {dist_dir}")


if __name__ == "__main__":
    main()
