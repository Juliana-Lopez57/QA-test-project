# AI-generated E2E vs manual improvements

This note compares what came from the **webTest-style prompts / AI-assisted workflow** (Prompts 1, 5, 6, 7) with **manual decisions** applied while making the suite stable and course-ready.

## What the AI / prompts produced well

- **Structure**: `conftest.py` with a `todo_page` fixture, a `TodoPage` page object, and separate `test_todo_crud.py` / `test_todo_filter.py` files matched the intended skeleton.
- **Stack**: Staying on **Python + pytest-playwright** (no TypeScript) was enforced in prompt text and kept consistently.
- **Locator direction**: Guidance to prefer Playwright’s role- and test-id-based locators aligned with how the official TodoMVC demo exposes `data-testid` attributes.

## What we changed manually (and why)

### 1. Filter journey order (`test_journey_03`)

**Issue:** On `#/active`, the demo removes completed rows from the DOM, so asserting “both tasks exist” after visiting Active first is fragile or wrong.

**Manual fix:** Reordered the flow to visit **Completed → All → Active** (and back to All), with a short comment in the test explaining the hash/DOM behavior.

**Lesson:** E2E stability often comes from **matching app routing rules**, not from the first scenario order the model suggests.

### 2. `TodoPage.list_titles()` behavior

**Issue:** A naive “always list every `todo-title`” helper fails under `#/active` and `#/completed` because the UI intentionally hides rows.

**Manual fix:** Implemented `list_titles()` with explicit branches for `#/active`, `#/completed`, and the default `#/` route, using completed vs non-completed row selectors where needed.

**Lesson:** Page objects should reflect **real URL/state semantics**, not a generic DOM dump.

### 3. Assertions: `expect` vs plain `assert`

**Manual choice:** Kept Playwright **`expect(...)`** for UI visibility, counts, classes, and URLs; used small **`assert`** checks where we only parse integers from stable text (`items_left_count()`).

**Lesson:** Prefer **`expect`** for anything the user sees; use **`assert`** sparingly for pure data derived from the page after the UI is already stable.

### 4. CI and local reproducibility

**Manual / iterative:** CI uses `python -m playwright install --with-deps chromium` so browser install does not depend on a `playwright` script being on `PATH`. Pull requests to `main` run the same job as pushes.

**Lesson:** Treat **CI as part of the test design**: install commands and triggers should mirror how developers run tests locally.

### 5. Reporting (Prompt 7)

**Manual step:** After a real `pytest` run, results were copied into `reports/latest-report.md` with the exact command and per-test lines from terminal output—no “green” claims without execution.

**Lesson:** The value of Prompt 7 is **evidence-first reporting**, not a narrative summary.

## Cursor skills used (webTest in `.cursor/skills/`)

These runs attach the official skill markdown with **`@`** so the agent follows jia’s workflow text, not only free-form prompts.

### `testing-qa` + `test-automator`

- **Goal:** Add a focused regression case with the same quality bar as the scenario docs.
- **Prompt (summary):** Extend `test_todo_crud.py` with `test_journey_05_cannot_add_whitespace_task`: submit whitespace-only input; assert no row, main/footer stay hidden, and no `todo-count` in the DOM.
- **Outcome:** New test + `TodoPage.submit_whitespace_only_task()`; stack stayed **Python + pytest-playwright**.

### `lint-and-validate`

- **Goal:** Review `week4-e2e-webtest/tests` for pytest/Playwright best practices (naming, assertions, structure) without adding new tests.
- **Outcome:** Used as a **read-only review** pass; any follow-up refactors (e.g. shared locators in the POM) were applied deliberately, not blindly.

**Lesson:** Skills are **conversation context** for Cursor; they do not get imported by pytest. The value is consistent checklists and role framing when extending the suite.

## Summary

| Area            | AI / prompt role              | Manual role                                      |
|-----------------|-------------------------------|--------------------------------------------------|
| Scenarios       | Breadth + template            | Selected P0 journeys, trimmed scope              |
| Skeleton        | File layout + placeholders    | Filled POM + tests                               |
| Stability       | Generic flows                 | Hash-aware ordering + `list_titles()` semantics  |
| CI              | —                             | Robust install command + `pull_request` trigger  |
| Report          | Format guidance               | Pasted real pytest output                        |
| Skills (`@`)    | `testing-qa`, `test-automator`, `lint-and-validate` | Whitespace journey + lint review of test folder |
