# CV Data Schema

Complete documentation of the YAML CV data structure.

## Structure Overview

```yaml
personal:
  name: string
  email: string
  phone: string (optional)
  location: string (optional)
  birth_date: string (optional)

summary: string

experience:
  - id: string
    company: string
    title: string
    period: string
    location: string (optional)
    technologies: [string] (optional)
    description: string

education:
  - id: string
    degree: string
    school: string (optional)
    graduation_year: number (optional)
    description: string (optional)

skills:
  - category: string
    items: [string]

certifications: (optional)
  - id: string
    title: string
    issuer: string
    issued_date: string (optional)
    expires_date: string (optional)

languages: (optional)
  - name: string
    level: string

projects: (optional)
  - id: string
    title: string
    description: string
    technologies: [string] (optional)
    url: string (optional)
```

## Detailed Sections

### Personal

```yaml
personal:
  name: John Doe                    # Full name (required)
  email: john@example.com           # Email address (required)
  phone: "+1 (555) 123-4567"        # Phone number (optional)
  location: San Francisco, CA       # City/Country (optional)
```

### Summary

Professional summary (2-3 sentences):

```yaml
summary: >
  Full-stack engineer with 8+ years of experience building scalable systems.
  Expertise in cloud infrastructure and DevOps. Passionate about automation
  and mentoring junior engineers.
```

Use `>` for multi-line text (preserves readability).

### Experience

```yaml
experience:
  - id: exp_1                       # Unique identifier (required)
    company: Tech Corp              # Company name (required)
    title: Senior Engineer          # Job title (required)
    period: 2021 - Present          # Time period (required)
    location: San Francisco, CA     # Location (optional)
    technologies:                   # Tech stack (optional)
      - Python
      - Kubernetes
      - AWS
    description: >                  # Job description (required)
      Led architecture of microservices platform.
      Mentored team of 4 engineers.
      Reduced latency by 40%.
```

**Tips:**

- Use descriptive verbs: "Built", "Led", "Designed", "Implemented"
- Include metrics: "reduced costs by 30%", "served 10M users"
- Keep descriptions 2-4 sentences

### Education

```yaml
education:
  - id: edu_1
    degree: B.S. Computer Science
    school: University of California
    graduation_year: 2016
    description: >
      Relevant coursework: Distributed Systems, Algorithms,
      Operating Systems.
```

### Skills

Organized by category:

```yaml
skills:
  - category: Backend
    items:
      - Python
      - Go
      - Java

  - category: DevOps
    items:
      - Kubernetes
      - Docker
      - Terraform

  - category: Databases
    items:
      - PostgreSQL
      - MongoDB
      - Redis
```

### Certifications

```yaml
certifications:
  - id: cert_1
    title: AWS Certified Solutions Architect
    issuer: Amazon Web Services
    issued_date: 2023-06-15
    expires_date: 2026-06-15
```

**Dates:** Use `YYYY-MM-DD` format or just `YYYY-MM`.

### Languages

```yaml
languages:
  - name: English
    level: Native

  - name: Spanish
    level: Fluent

  - name: Mandarin
    level: Basic
```

**Levels:** Native, Fluent, Intermediate, Basic

### Projects

```yaml
projects:
  - id: proj_1
    title: Open Source Kubernetes Operator
    description: >
      Automated database management operator for Kubernetes.
      10k+ downloads.
    technologies:
      - Go
      - Kubernetes
    url: "https://github.com/example/db-operator"
```

## Validation Rules

- **Required fields:** Must be present (see schema above)
- **Email:** Must be valid email format
- **IDs:** Must be unique within each section
- **YAML format:** Proper indentation (2 spaces), no tabs

## Examples

### Example 1: Senior Engineer

```yaml
personal:
  name: Alice Johnson
  email: alice@example.com
  phone: "+1 (555) 987-6543"
  location: San Francisco, CA

summary: >
  Seasoned full-stack engineer with 10+ years building large-scale distributed systems.
  Proven track record of technical leadership and mentoring. Expertise in cloud
  infrastructure, microservices, and team building.

experience:
  - id: exp_1
    company: Big Tech Corp
    title: Staff Engineer
    period: 2019 - Present
    location: San Francisco, CA
    technologies:
      - Python
      - Go
      - Kubernetes
      - PostgreSQL
      - AWS
    description: >
      Leading infrastructure initiatives for platform serving 100M+ users.
      Designed and implemented event streaming system processing 1M+ events/sec.
      Established SRE practices reducing incidents by 60%. Mentored 6 engineers
      to promotion.
```

### Example 2: Recent Graduate

```yaml
personal:
  name: Bob Smith
  email: bob@example.com
  location: New York, NY

summary: >
  Recent computer science graduate passionate about web development and open source.
  Strong foundation in full-stack development. Eager to learn and contribute to
  impactful projects.

education:
  - id: edu_1
    degree: B.S. Computer Science
    school: New York University
    graduation_year: 2024
    description: >
      GPA: 3.8. Dean's List all semesters. Senior thesis on distributed systems.

experience:
  - id: exp_1
    company: StartupXYZ
    title: Software Engineering Intern
    period: 2023 - 2024
    location: New York, NY
    technologies:
      - React
      - Node.js
      - PostgreSQL
    description: >
      Built React components for analytics dashboard. Implemented REST API
      endpoints using Node.js. Participated in daily standups and code reviews.
```

## Multi-Language

For French and Italian, simply translate all text:

```yaml
# cv_fr.yml
personal:
  name: Jean Dupont
  email: jean@example.com
  location: Paris, France

summary: >
  Ingénieur informatique avec 8+ années d'expérience...

experience:
  - id: exp_1
    company: TechCorp
    title: Ingénieur Senior
    period: 2021 - Présent
    description: >
      Dirigé l'architecture d'une plateforme microservices...
```

## Tips & Best Practices

1. **Use action verbs:**
   - Designed, Built, Implemented, Led, Managed, Optimized, Reduced, Increased

2. **Include metrics:**
   - "Reduced latency by 40%"
   - "Served 10M users"
   - "Processed 1M events/sec"

3. **Be specific:**
   - ❌ "Worked on infrastructure"
   - ✅ "Designed Kubernetes cluster managing 500 microservices"

4. **Update regularly:**
   - Add new experiences as they happen
   - Update current role period to "Present"
   - Keep skills up-to-date

5. **Keep it scannable:**
   - Use bullet points for descriptions
   - Limit to 2-4 sentences per job
   - Organize skills by relevance

## Validation

Validate your YAML:

```bash
python backend/generate.py
```

Errors will indicate schema problems.

---

For more help, see [GETTING_STARTED.md](GETTING_STARTED.md) or open an [Issue](https://github.com/YOUR_USERNAME/resume-as-code/issues).
