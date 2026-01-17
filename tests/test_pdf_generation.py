"""
Basic tests for CV generation functionality.
"""

import tempfile
from pathlib import Path

from backend.generators.pdf_generator import create_pdf_html, generate_pdf
from backend.parsers.schema import validate_cv
from backend.parsers.yaml_parser import parse_cv_file


def test_pdf_generation():
    """Test that PDF generation works for all available languages."""
    cv_data_dir = Path(__file__).parent.parent / "cv-data"

    # Load UI translations
    ui_translations_file = cv_data_dir / "ui_translations.yml"
    ui_translations = parse_cv_file(str(ui_translations_file))

    # Discover available CV files dynamically
    cv_files = list(cv_data_dir.glob("cv_*.yml"))
    assert len(cv_files) > 0, "No CV files found in cv-data directory"

    for cv_file in cv_files:
        # Extract language code from filename (cv_en.yml -> en)
        lang = cv_file.stem.replace("cv_", "")

        # Parse CV data
        cv_data = parse_cv_file(str(cv_file))
        cv_data = validate_cv(cv_data).model_dump()
        cv_data["translations"] = ui_translations

        # Generate PDF HTML
        html_content = create_pdf_html(cv_data, lang)

        # Check that HTML contains expected elements
        assert "<!DOCTYPE html>" in html_content
        assert cv_data["personal"]["name"] in html_content
        assert "Inter" in html_content  # Check for professional font

        # Generate actual PDF to temp file
        with tempfile.NamedTemporaryFile(suffix=".pdf", delete=False) as f:
            pdf_path = f.name

        generate_pdf(cv_data, pdf_path, lang)
        pdf_file = Path(pdf_path)
        assert pdf_file.exists(), f"PDF file was not generated for {lang}"
        assert pdf_file.stat().st_size > 0, f"PDF file is empty for {lang}"
        pdf_file.unlink()  # Clean up

        print(f"✓ PDF generation test passed for {lang.upper()}")


def test_pdf_styling():
    """Test that PDF has professional styling."""
    cv_data_dir = Path(__file__).parent.parent / "cv-data"

    # Load UI translations
    ui_translations_file = cv_data_dir / "ui_translations.yml"
    ui_translations = parse_cv_file(str(ui_translations_file))

    # Use first available CV file
    cv_files = list(cv_data_dir.glob("cv_*.yml"))
    assert len(cv_files) > 0, "No CV files found"
    cv_file = cv_files[0]
    lang = cv_file.stem.replace("cv_", "")

    cv_data = parse_cv_file(str(cv_file))
    cv_data = validate_cv(cv_data).model_dump()
    cv_data["translations"] = ui_translations

    html_content = create_pdf_html(cv_data, lang)

    # Check for professional styling elements
    assert "font-family: 'Inter'" in html_content
    assert "#2563eb" in html_content  # Professional blue color
    assert "text-align: center" in html_content  # Centered header
    assert "border-bottom: 3px solid #2563eb" in html_content  # Header underline
    assert "page-break-inside: avoid" in html_content  # Page break control

    print("✓ PDF styling test passed")


if __name__ == "__main__":
    test_pdf_generation()
    test_pdf_styling()
    print("✅ All PDF tests passed!")
