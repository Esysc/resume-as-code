# Frequently Asked Questions

## General

**Q: Is CV as Code free?**
A: Yes! It's MIT licensed and open source.

**Q: Can I use it privately?**
A: Yes. Keep your repo private—only publish the CV.

**Q: Do I need to be a developer?**
A: Not necessarily. Edit YAML files and push to GitHub. No coding required!

**Q: How do I keep my CV updated?**
A: Edit `cv-data/cv_en.yml` and push to GitHub. Changes deploy automatically.

## Setup

**Q: What if I have errors running generate.py?**
A: Ensure Python 3.9+ and all dependencies are installed:

```bash
pip install -r backend/requirements.txt
```

**Q: Can I deploy somewhere other than GitHub Pages?**
A: Yes! The `dist/` folder is fully static—deploy to Netlify, Vercel, or any host.

**Q: How do I update the public CV?**
A: Just push to `main` branch. GitHub Actions auto-deploys.

## Customization

**Q: How do I change colors?**
A: Edit `web/src/styles/App.css` and update CSS variables.

**Q: Can I use a custom domain?**
A: Yes. See GitHub Pages documentation.

**Q: How do I add new sections?**
A: Add fields to YAML, then update `web/src/App.jsx` and `backend/templates/cv.html`.

## Multi-Language

**Q: How do I add a new language?**
A: Create `cv-data/cv_XX.yml` (where XX is language code), add translation,
update language selector in `web/src/App.jsx`.

**Q: Do I need to maintain three separate CVs?**
A: Yes, but they can share structure—just translate the text.

## PDFs & Exports

**Q: How do I generate role-specific PDFs?**
A: Create a local Git branch, edit YAML, run `generate.py`, don't push. See [GETTING_STARTED.md](GETTING_STARTED.md#creating-role-specific-pdfs-local).

**Q: Can I download the PDF?**
A: PDF is generated in `dist/cv_en.pdf` during build. Share it from there.

**Q: Can I add custom fonts to PDF?**
A: WeasyPrint supports Google Fonts and system fonts. Edit `backend/generators/pdf_generator.py`.

## Contributing

**Q: How do I contribute?**
A: See [CONTRIBUTING.md](../CONTRIBUTING.md).

**Q: What kind of contributions are needed?**
A: Templates, translations, documentation, features, bug fixes.

**Q: Can I create a template?**
A: Absolutely! See Contributing guidelines for details.

## Troubleshooting

**Q: My CV isn't updating on GitHub Pages**
A:

1. Check GitHub Actions logs
2. Ensure changes are pushed to `main`
3. Wait 30 seconds and refresh browser cache

**Q: "Module not found" errors**
A: Install dependencies:

```bash
pip install -r backend/requirements.txt
npm install
```

**Q: PDF looks weird**
A: WeasyPrint doesn't support all CSS. Stick to basic styles. See docs for limitations.

**Q: Changes work locally but not on Pages**
A: Did you commit and push? GitHub Actions only runs on pushes.

## Best Practices

**Q: How often should I update my CV?**
A: Treat it like code—commit milestones, promotions, new skills.

**Q: Should I make my repo public?**
A: Yes! Show the world you use infrastructure-as-code.
Keep personal data in commits, not published.

**Q: What if I change jobs?**
A: Edit `cv-data/cv_en.yml`:

1. Add new experience entry
2. Update dates on previous role (change "Present" to end date)
3. Update summary if needed
4. Push to GitHub

**Q: Can I use this for portfolio instead of CV?**
A: Yes! Add projects section and customize layout.

---

Still have questions? [Open an Issue](https://github.com/YOUR_USERNAME/resume-as-code/issues)!
