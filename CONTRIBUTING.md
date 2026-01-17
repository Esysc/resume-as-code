# Contributing to Resume as Code

Thank you for your interest in contributing! We welcome all kinds of contributions:

- 🐛 **Bug reports** and fixes
- ✨ **New features** and improvements
- 📝 **Documentation** enhancements
- 🎨 **Templates** and themes
- 🌍 **Translations** to new languages
- 💡 **Ideas** and suggestions

## Code of Conduct

Please be respectful and constructive. We're building a welcoming community.

## Getting Started

### 1. Fork the Repository

```bash
git clone https://github.com/YOUR_FORK/cv-as-code.git
cd cv-as-code
```

### 2. Create a Feature Branch

```bash
git checkout -b feature/your-feature-name
```

Use clear branch names:

- `feature/new-template` — New template
- `fix/language-switch-bug` — Bug fix
- `docs/deployment-guide` — Documentation
- `i18n/spanish-translation` — Translation

### 3. Make Your Changes

Follow these guidelines:

#### Python (Backend)

```python
# Use type hints
def generate_html(cv_data: dict) -> str:
    """Generate HTML from CV data.

    Args:
        cv_data: Parsed CV data dictionary

    Returns:
        HTML string
    """
    # Implementation
    return html
```

#### JavaScript/React (Frontend)

```javascript
// Use functional components with hooks
export function LanguageSelector({ currentLang, onLangChange }) {
  return (
    <select value={currentLang} onChange={(e) => onLangChange(e.target.value)}>
      <option value="en">English</option>
      <option value="fr">Français</option>
    </select>
  );
}
```

#### Documentation

- Use clear, concise language
- Include code examples
- Add table of contents for long docs
- Keep lines under 100 characters where possible

### 4. Test Your Changes

```bash
# Backend tests
cd backend
pytest tests/

# Frontend tests
cd ../web
npm test

# Manual testing
python backend/generate.py
cd web && npm run dev
```

### 5. Commit Messages

Write clear commit messages:

```bash
git commit -m "feat: add support for certifications section"
git commit -m "fix: language selector not persisting to localStorage"
git commit -m "docs: add customization guide"
git commit -m "refactor: simplify HTML generator"
```

Use conventional commits:

- `feat:` — New feature
- `fix:` — Bug fix
- `docs:` — Documentation
- `refactor:` — Code improvement
- `test:` — Test additions
- `style:` — Formatting changes

### 6. Push and Create a Pull Request

```bash
git push origin feature/your-feature-name
```

Then open a PR on GitHub with:

- Clear title
- Description of changes
- Motivation/context
- Screenshots (if UI changes)
- Checklist of testing

## PR Checklist

Before submitting, ensure:

- [ ] Code follows project style
- [ ] Tests pass (`pytest` + `npm test`)
- [ ] Documentation is updated
- [ ] No breaking changes (or clear migration guide)
- [ ] Commit messages are clear
- [ ] Changes are focused on one feature/fix

## Development Setup

### Backend

```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

### Frontend

```bash
cd web
nvm use 18  # Use Node 18+
npm install
npm run dev
```

### Running Tests

```bash
# Backend
cd backend && pytest tests/ -v

# Frontend
cd web && npm test

# Full test suite
make test
```

## Areas We Need Help With

### 🎨 Templates

Add new resume templates (e.g., `minimal`, `sidebar`, `creative`):

```text
backend/templates/
├── cv.html              # Current (modern)
├── cv_minimal.html      # New template
├── cv_sidebar.html      # New template
└── cv_creative.html     # New template
```

### 🌍 Translations

Add translations for new languages:

```yaml
# cv-data/cv_es.yml
personal:
  name: Tu Nombre
  email: tu@email.com

# Update backend/parsers/schema.py to support es
```

### 📝 Documentation

- Deployment guides (Netlify, Vercel, AWS)
- Tutorial videos
- Use case examples
- Advanced customization

### 🐛 Known Issues

See [Issues](https://github.com/YOUR_USERNAME/cv-as-code/issues)
for bugs we're aware of.

## Questions?

- Comment on related issues
- Open a discussion
- Email maintainers

## License

By contributing, you agree your code will be licensed under MIT License.

---

**Thank you for making CV as Code better!** 🎉
