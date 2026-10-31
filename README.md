# Field Courses

Free, interactive courses on **DevOps, SRE, platform engineering, AI agents and security**.

Each course explains the ideas that matter in plain language, then lets you try them: simulators, calculators, sorting exercises and checkpoint questions that explain the answer. Courses run entirely in your browser. No sign-up, no tracking, and your progress is saved locally.

**Live site:** https://jazeer888.github.io/field-courses/

## Courses

| Course | Type | Modules | Time | Status |
|---|---|---|---|---|
| [SRE Workbook](https://jazeer888.github.io/field-courses/courses/sre-workbook/) | Book companion | 11 | ~50 min | Available |
| [AI Agent Security](https://jazeer888.github.io/field-courses/courses/ai-agent-security/) | Topic (beginner) | 10 | ~55 min | Available |
| Platform Engineering | Topic | – | – | Planned |

Want a course on something else? [Request one](https://github.com/jazeer888/field-courses/issues/new?template=course-request.md).

## How every course works

- **Plain words first.** Each concept opens with an everyday comparison, then the precise version.
- **Learn by doing.** Hands-on widgets show cause and effect, such as an error budget simulator or a burn-rate explorer.
- **Checkpoints.** Each module ends with a question; your first answer counts, and the explanation shows why.
- **Progress to completion.** A final review module gives a cheat sheet, your score per module, and what to read next.

## Run locally

Each course is a single, self-contained HTML file.

```bash
git clone https://github.com/jazeer888/field-courses.git
cd field-courses
python3 -m http.server 8000   # then open http://localhost:8000
```

You can also open any `courses/<name>/index.html` file directly in a browser.

## Repository layout

```
index.html                 course catalog
courses/<slug>/index.html  one self-contained course per folder
tests/smoke.py             clicks through every course step and fails on errors or overflow
.github/workflows/ci.yml   runs the smoke test and deploys to GitHub Pages
```

## Contributing

Corrections are the most valuable contribution. If something is wrong or unclear, [report it](https://github.com/jazeer888/field-courses/issues/new?template=error-report.md). See [CONTRIBUTING.md](CONTRIBUTING.md) for how to propose or add a course.

## License

- Code: [MIT](LICENSE)
- Course content: [CC BY 4.0](LICENSE-CONTENT.md). Reuse it freely with attribution.

Book companion courses are independent study guides. They paraphrase and cite their source books and are not affiliated with the authors or publishers. No book text is included in this repository.
