# Week 4 — Web E2E (Playwright + pytest)

Self-contained **end-to-end** tests against the public Playwright **TodoMVC** demo:

https://demo.playwright.dev/todomvc/

This folder includes a Page Object, `pytest-playwright` tests, AI workflow artifacts (`ai-workflow/`), and reports under `reports/`. The workflow follows the [webTest](https://github.com/jia57b/webTest) guide, adapted to **Python** (not TypeScript).

## Requirements

- **Python 3.12+** (on macOS the command is usually `python3`).
- Root repository dependencies (includes `playwright` and `pytest-playwright`).

Optional: virtual environment at the repo root (`.venv/`).

## Setup

From the **repository root** (`QA-TEST-PROJECT`):

```bash
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt
python3 -m playwright install
```

Chromium only (faster first install):

```bash
python3 -m playwright install chromium
```

## Running tests

Still from the repository root:

```bash
python3 -m pytest week4-e2e-webtest/tests -v
```

Retain traces only on failure (useful for debugging):

```bash
python3 -m pytest week4-e2e-webtest/tests -v --tracing=retain-on-failure
```

## Directory layout

| Path | Purpose |
|------|---------|
| `pages/todo_page.py` | Page Object Model (locators and actions) |
| `tests/conftest.py` | Fixtures (`todo_page`, `base_url`) |
| `tests/test_todo_crud.py` | P0 journeys (create, complete, filters, clear completed, whitespace-only input) |
| `tests/test_todo_filter.py` | Additional filter scenarios |
| `ai-workflow/` | Saved prompts and notes (scenarios, skeleton, code, report, AI vs manual) |
| `reports/latest-report.md` | Latest integration-style report from a real run |

## webTest (jia) guide — path mapping

The upstream guide suggests generic paths; this project uses:

| Guide (example) | This project |
|-----------------|--------------|
| `docs/testing/e2e-scenarios.md` | `ai-workflow/prompt1-scenarios.md` |
| `tests/e2e/specs/*.spec.ts` | `tests/test_*.py` (pytest-playwright) |
| `reports/e2e/latest-report.md` | `reports/latest-report.md` |

## Cursor skills (webTest in the repo)

Skills from the **webTest** repository live under **`.cursor/skills/`** (for example `testing-qa`, `playwright-skill`, …). In Cursor chat, reference them with **`@`** on the file, for example:

`.cursor/skills/testing-qa/SKILL.md`

That matches prompts that say `Use @testing-qa` (replace with a real `@` reference to the `SKILL.md` path).

**Example:** attach `.cursor/skills/testing-qa/SKILL.md` and `.cursor/skills/test-automator/SKILL.md` when asking the agent to add or refine a test; attach `.cursor/skills/lint-and-validate/SKILL.md` when you want a **review-only** pass over `tests/` (no new tests).

## Continuous integration

The E2E workflow is at the repository root:

`.github/workflows/e2e-test.yml`

It installs dependencies, runs `python -m playwright install --with-deps chromium`, executes the same tests, and uploads artifacts (`test-results`, etc.) when applicable.

## Other course documentation

- API / CI notes: `docs/` (week1–week3).
- AI vs manual adjustments: `ai-workflow/ai-vs-manual-review.md`.
