import { useState, useEffect } from "react";
import "./styles/App.css";
import html2pdf from "html2pdf.js";

function App() {
  const [cvData, setCvData] = useState(null);
  const [currentLang, setCurrentLang] = useState("en");
  const [isDarkMode, setIsDarkMode] = useState(false);

  useEffect(() => {
    // Load CV data for current language
    fetch(`/cv_${currentLang}.json`)
      .then((res) => {
        if (!res.ok) {
          throw new Error(`HTTP error! status: ${res.status}`);
        }
        return res.json();
      })
      .then((data) => {
        console.log("Loaded CV data:", data);
        setCvData(data);
      })
      .catch((err) => {
        console.error("Failed to load CV:", err);
        setCvData(null);
      });
  }, [currentLang]);

  const downloadPDF = () => {
    // Hide navigation and header actions for PDF
    const nav = document.querySelector("nav");
    const headerActions = document.querySelector(".header-actions");
    const originalNavDisplay = nav.style.display;
    const originalActionsDisplay = headerActions.style.display;
    nav.style.display = "none";
    headerActions.style.display = "none";

    const element = document.querySelector(".app");
    const name = cvData.personal.name.replace(/\s+/g, "_");
    const options = {
      margin: 0.5,
      filename: `${name}_CV_${currentLang}.pdf`,
      image: { type: "jpeg", quality: 0.98 },
      html2canvas: { scale: 2 },
      jsPDF: { unit: "in", format: "letter", orientation: "portrait" },
    };
    html2pdf()
      .set(options)
      .from(element)
      .save()
      .then(() => {
        // Restore navigation and header actions
        nav.style.display = originalNavDisplay;
        headerActions.style.display = originalActionsDisplay;
      });
  };

  if (!cvData) {
    return (
      <div className="container">
        <p>Loading...</p>
      </div>
    );
  }

  if (!cvData.translations || !cvData.translations[currentLang]) {
    return (
      <div className="container">
        <p>Error: Translations not found for {currentLang}</p>
      </div>
    );
  }

  return (
    <div className="app">
      <header className="header">
        <div className="container">
          <div className="header-content">
            <div>
              <h1>{cvData.personal.name}</h1>
              <p className="contact-info">{cvData.personal.location}</p>
            </div>
            <div className="header-actions">
              <button onClick={downloadPDF} className="download-btn">
                📄 Download PDF
              </button>
              <select
                value={currentLang}
                onChange={(e) => setCurrentLang(e.target.value)}
              >
                <option value="en">English</option>
                <option value="fr">Français</option>
                <option value="it">Italiano</option>
              </select>
              <button onClick={() => setIsDarkMode(!isDarkMode)}>
                {isDarkMode ? "☀️" : "🌙"}
              </button>
            </div>
          </div>
        </div>
      </header>

      <main className="container">
        <nav className="nav">
          <a href="#experience">
            {cvData.translations[currentLang].experience}
          </a>
          <a href="#education">{cvData.translations[currentLang].education}</a>
          <a href="#skills">{cvData.translations[currentLang].skills}</a>
          <a href="#projects">{cvData.translations[currentLang].projects}</a>
          <a href="#certifications">
            {cvData.translations[currentLang].certifications}
          </a>
        </nav>

        <section className="summary">
          <p>{cvData.summary}</p>
        </section>

        <section className="section">
          <h2 id="experience">{cvData.translations[currentLang].experience}</h2>
          {cvData.experience.map((exp) => (
            <div key={exp.id} className="entry">
              <h3>
                {exp.title} <span className="company">@ {exp.company}</span>
              </h3>
              <p className="meta">
                {exp.period} | {exp.location}
              </p>
              <p className="description">{exp.description}</p>
              {exp.technologies && (
                <div className="technologies">
                  {exp.technologies.map((tech) => (
                    <span key={tech} className="tech-badge">
                      {tech}
                    </span>
                  ))}
                </div>
              )}
            </div>
          ))}
        </section>

        <section className="section">
          <h2 id="education">{cvData.translations[currentLang].education}</h2>
          {cvData.education.map((edu) => (
            <div key={edu.id} className="entry">
              <h3>{edu.degree}</h3>
              <p className="meta">
                {edu.school} ({edu.graduation_year})
              </p>
              {edu.description && (
                <p className="description">{edu.description}</p>
              )}
            </div>
          ))}
        </section>

        <section className="section">
          <h2 id="skills">{cvData.translations[currentLang].skills}</h2>
          <div className="skills-grid">
            {cvData.skills.map((skillGroup, idx) => (
              <div key={idx} className="skill-category">
                <h3>{skillGroup.category}</h3>
                <ul>
                  {skillGroup.items.map((item) => (
                    <li key={item}>{item}</li>
                  ))}
                </ul>
              </div>
            ))}
          </div>
        </section>

        {cvData.projects && cvData.projects.length > 0 && (
          <section className="section">
            <h2 id="projects">{cvData.translations[currentLang].projects}</h2>
            {cvData.projects.map((proj) => (
              <div key={proj.id} className="entry">
                <h3>{proj.title}</h3>
                <p className="description">{proj.description}</p>
                {proj.technologies && (
                  <div className="technologies">
                    {proj.technologies.map((tech) => (
                      <span key={tech} className="tech-badge">
                        {tech}
                      </span>
                    ))}
                  </div>
                )}
                {proj.url && (
                  <p>
                    <a
                      href={proj.url}
                      target="_blank"
                      rel="noopener noreferrer"
                    >
                      {proj.url}
                    </a>
                  </p>
                )}
              </div>
            ))}
          </section>
        )}

        {cvData.certifications && cvData.certifications.length > 0 && (
          <section className="section">
            <h2 id="certifications">
              {cvData.translations[currentLang].certifications}
            </h2>
            {cvData.certifications.map((cert) => (
              <div key={cert.id} className="entry">
                <h3>{cert.title}</h3>
                <p className="meta">
                  {cert.issuer} | {cert.issued_date}
                </p>
              </div>
            ))}
          </section>
        )}
      </main>
    </div>
  );
}

export default App;
