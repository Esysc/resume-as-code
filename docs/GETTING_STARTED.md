# Getting Started with CV as Code

This guide will walk you through setting up your own Resume-as-Code instance.

## Prerequisites

- Python 3.9+
- Node.js 18+
- Git
- GitHub account

## Step 1: Fork or Clone

### Option A: Fork on GitHub (Recommended for public resume)

1. Go to [resume-as-code](https://github.com/YOUR_USERNAME/resume-as-code)
2. Click **Fork** button
3. Clone your fork:

   ```bash
   git clone https://github.com/YOUR_USERNAME/resume-as-code.git
   cd resume-as-code
   ```

### Option B: Clone

```bash
git clone https://github.com/YOUR_USERNAME/resume-as-code.git
cd resume-as-code
```

## Step 2: Setup Environment

### Backend

```bash
# Create virtual environment
python -m venv venv

# Activate it
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r backend/requirements.txt
```

### Frontend

```bash
cd web
npm install
cd ..
```

## Step 3: Customize Your CV

Edit `cv-data/cv_en.yml`:

```yaml
personal:
  name: Your Name
  email: your.email@example.com
  phone: "+1 (555) 123-4567"
  location: City, Country

summary: >
  Your professional summary here...

experience:
  - id: exp_1
    company: Your Company
    title: Your Job Title
    period: 2020 - Present
    location: City, Country
    technologies:
      - Python
      - Kubernetes
    description: >
      Your accomplishments and responsibilities...
```

See [CV_SCHEMA.md](CV_SCHEMA.md) for complete field documentation.

### Add Other Languages

Edit `cv-data/cv_fr.yml` (French) and `cv-data/cv_it.yml` (Italian)
following the same format.

## Step 4: Generate Outputs

```bash
python backend/generate.py
```

This creates:

- `dist/cv_en.html` — Static HTML
- `dist/cv_en.json` — JSON data
- `dist/cv_en.pdf` — PDF document

(Plus `_fr` and `_it` variants if you created them)

## Step 5: Preview Locally

```bash
# Start development server
cd web && npm run dev
```

Open <http://localhost:3000> in your browser.

## Step 6: Deploy to GitHub Pages

### 1. Enable GitHub Pages

In your repository settings:

1. Go to **Settings** → **Pages**
2. Set **Source** to **GitHub Actions**
3. Save

### 2. Push to GitHub

```bash
git add .
git commit -m "Initial CV setup"
git push origin main
```

GitHub Actions will automatically:

1. Generate HTML/JSON/PDF
2. Build React app
3. Deploy to GitHub Pages

### 3. View Your CV

Your resume is now live at: `https://YOUR_USERNAME.github.io/resume-as-code`

## Workflow: Updating Your CV

### 1. Edit YAML

```bash
nano cv-data/cv_en.yml
```

### 2. Test Locally

```bash
python backend/generate.py
cd web && npm run dev
```

### 3. Commit and Push

```bash
git add cv-data/cv_en.yml
git commit -m "Update: Added new project"
git push origin main
```

✅ Your CV is updated automatically!

## Creating Role-Specific PDFs (Local)

For targeted job applications, create local branches:

```bash
# Create branch for specific role
git checkout -b feature/cv-manager

# Edit cv_en.yml to emphasize leadership, mentoring
nano cv-data/cv_en.yml

# Generate PDF
python backend/generate.py

# Send dist/cv_en.pdf to recruiter
# Don't push this branch
git checkout main
git branch -d feature/cv-manager
```

## Customization

### Change Colors

Edit `web/src/styles/App.css`:

```css
:root {
  --primary: #2563eb;    /* Main color */
  --secondary: #1e40af;  /* Secondary */
  --accent: #f97316;     /* Accent */
}
```

### Change Fonts

Edit `web/src/styles/App.css`:

```css
body {
  font-family: 'Your Font', sans-serif;
}
```

### Change Layout

Edit `backend/templates/cv.html` (HTML structure) or `web/src/App.jsx` (React layout).

## Troubleshooting

### "ModuleNotFoundError: No module named 'pydantic'"

```bash
pip install -r backend/requirements.txt
```

### "npm: command not found"

Install Node.js from <https://nodejs.org>

### PDF not generating

Check that WeasyPrint is installed:

```bash
pip install WeasyPrint
```

### Changes not showing

1. Run generator: `python backend/generate.py`
2. Rebuild frontend: `cd web && npm run build`
3. Push to GitHub: `git push`
4. Wait 30 seconds for GitHub Actions to complete

## Next Steps

- Read [CUSTOMIZATION.md](CUSTOMIZATION.md) for advanced styling
- Check [ROADMAP.md](ROADMAP.md) for planned features
- See [CONTRIBUTING.md](../CONTRIBUTING.md) to contribute

## Questions?

- Open an [Issue](https://github.com/YOUR_USERNAME/resume-as-code/issues)
- Check the [FAQ](FAQ.md)

---

Happy CV-ing! 🎉
