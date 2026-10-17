# Contributing to Field Courses

Thanks for helping. Accuracy matters more than anything else here, so corrections are always welcome.

## Report an error

Open an [error report](https://github.com/jazeer888/field-courses/issues/new?template=error-report.md) with the course, module and step (shown as `3.2` at the bottom of each step), what's wrong, and a source if you have one.

## Request a course

Open a [course request](https://github.com/jazeer888/field-courses/issues/new?template=course-request.md). Upvote existing requests with a 👍 reaction so we know what to build next.

## Add or change a course

1. Create `courses/<slug>/index.html` as a single self-contained file. Copy `courses/sre-workbook/index.html` as the starting point and replace the content array (`M`), widgets and results checklist.
2. Give it a unique progress key, e.g. `course-<slug>-v1`.
3. Add a card to `index.html` and a row to the table in `README.md`.
4. Run the smoke test (below) and open a pull request.

### Quality bar

Every course must:

- **Explain simply.** Concept steps start with an "In plain words" box using an everyday comparison, then give the precise version. Define every term on first use.
- **Be interactive.** At least one checkpoint per module, and hands-on widgets wherever there's a number, mechanism or trade-off to explore.
- **Lead to completion.** Module 0 "Start here", core modules in prerequisite order, and a "Final review" with a cheat sheet and results.
- **Be correct.** Quiz answers have one clearly right option and an explanation. Numbers in widgets are checked.
- **Respect copyright.** Book companions paraphrase and cite; never paste book text. Quote at most a sentence.
- **Work everywhere.** Phone width (about 400px), light and dark mode, keyboard navigation.

### Run the smoke test

```bash
pip install playwright
python -m playwright install chromium
python tests/smoke.py
```

It loads every course, clicks through every step and fails on JavaScript errors or horizontal scrolling at phone width. CI runs the same test on every pull request.
