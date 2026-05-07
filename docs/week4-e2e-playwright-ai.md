# Week 4: End-to-End (E2E) Web Testing with Playwright & AI

## 1. Objective
Learn how to design, implement, and maintain an End-to-End UI testing framework for a web application (TodoMVC) using Python, pytest-playwright, and AI-assisted workflows.

## 2. Key Concepts Mastered

### AI-Assisted QA Architecture
- **Prompt Engineering & Guardrails:** Learned how to guide an AI agent (Cursor) to generate code that strictly adheres to an existing tech stack (Python/Pytest), preventing it from defaulting to its standard Node.js/TypeScript training.
- **Skills Integration:** Implemented a hybrid approach for AI context management. Used "Prompt Files" (Option C) for an audit trail, and later integrated native `.cursor/skills/` to provide the AI with strict Senior QA checklists for edge cases and linting.
- **Gap Analysis & Refactoring:** Used AI not just to write code, but to *audit* it. Applied a "Senior QA Linting" pass to refactor standard `assert` statements into Playwright's native `expect()` for better UI resilience.

### Playwright & UI Testing Best Practices
- **User Journeys vs. Test Cases:** Shifted focus from isolated test cases to critical "User Journeys" (P0), testing complete business flows (e.g., Create -> Complete -> Filter -> Clear) to avoid test bloat.
- **Page Object Model (POM):** Abstracted UI locators and actions into a `TodoPage` class to keep test files clean and maintainable.
- **Stable Locators & Auto-Wait:** Prioritized stable user-facing locators (`get_by_placeholder`, `get_by_test_id`, `get_by_role`) and eliminated manual `time.sleep()`, relying completely on Playwright's auto-wait mechanisms.
- **State and DOM Awareness:** Handled complex UI behaviors, such as elements being dynamically removed from the DOM during routing (e.g., TodoMVC filter tabs), by explicitly ordering test steps to match app behavior.

## 3. CI/CD Integration
- Successfully integrated E2E tests into GitHub Actions using the `ubuntu-latest` environment.
- Learned the critical importance of using `playwright install --with-deps chromium` in CI pipelines to ensure Linux operating system dependencies for headless browsers are properly installed.

## 4. Deliverables Completed
- ✅ `week4-e2e-webtest/tests/`: E2E suite with five CRUD journeys (including one whitespace-only edge case) plus three filter-focused tests (**eight tests** total).
- ✅ `week4-e2e-webtest/pages/`: Page Object Model implementation.
- ✅ `week4-e2e-webtest/reports/`: AI-generated execution reports reflecting real terminal output.
- ✅ `week4-e2e-webtest/ai-workflow/`: Documentation of the AI prompt process and manual interventions.
- ✅ `.github/workflows/e2e-test.yml`: Fully functional CI pipeline.