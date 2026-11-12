# Boris Brodski

**Software architect · AI security** — Düsseldorf, Germany · [brodski.name](https://brodski.name) · [openbrod.org](https://openbrod.org) · Boris@Brodski.name

Security from the transistor to the model. Twenty-five years from a cryptographic file layer (2001) and a degree focused on *security and verification*, through eleven years as chief architect of a backend platform for the German tax administration, to AI security today: trojaned open-weight models, agent harnesses, and **Torhaus** — a secure host for untrusted AI agents.

| Direction | What you'll find |
|---|---|
| [Security & AI security](https://brodski.name/security/) | Cryptographic design, reverse engineering (x86, OllyDbg, Java bytecode), hardened architectures, AI-security talk, Torhaus |
| [AI & machine learning](https://brodski.name/ai/) | Vision models from data collection to customer app, trading models, LoRA fine-tuning, local agent harnesses |
| [Languages & DSLs](https://brodski.name/languages/) | IDScript (a language built from parser to IDE), Xtext since 2006, Langium, [xtextcasts.org](https://xtextcasts.org) |
| [Java enterprise](https://brodski.name/java/) | Chief architect on KONSENS since 2012; JBoss EAP, Hibernate, Eclipse RCP, Vaadin, 15+ engineers |
| [Python & Django](https://brodski.name/django/) | Django in production, Python ↔ C++ bridges, ML pipelines |
| [Ruby on Rails](https://brodski.name/rails/) | Redmine plugin suites, plugin audits, hosting; Puppet |
| [Microcontrollers & IoT](https://brodski.name/embedded/) | PIC assembler and C++ since 1997, Arduino, Bluetooth LE |
| [Systems & C/C++](https://brodski.name/systems/) | An OS kernel at 19, 7-Zip-JBinding (JNI), cross-platform builds |
| [Open source](https://brodski.name/open-source/) | 7-Zip-JBinding, Redmine plugins, xtextcasts.org, Torhaus — all under openbrod.org |
| [Full CV](https://brodski.name/cv/) | Every project since 2001, skills timeline, education, talks |

---

## This repository

Source of [brodski.name](https://brodski.name): a static site generated from plain data files, so each direction page is a filtered view of one dataset.

```
data/        site.yaml, projects.yaml, skills.yaml, talks.yaml, education.yaml  — the single source of truth
pages/       one Markdown file per page: front matter (title, lead, pitch) + narrative
templates/   Jinja2: base, index, direction, cv, 404
static/      style.css, favicon, cv/ (PDF downloads)
build.py     ~150 lines; writes _site/
```

```sh
make deps     # pip install jinja2 pyyaml markdown
make serve    # build and open http://localhost:8000
```

Pushing to `main` builds and deploys through GitHub Actions (`.github/workflows/pages.yml`). PDF downloads are picked up automatically when placed in `static/cv/`: `boris-brodski-<direction>.pdf` for the one-page CVs, and any `*-de.pdf` for the full German profile.
