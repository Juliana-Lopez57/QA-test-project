Act as a QA E2E Expert and Playwright automation engineer. Implement the full Playwright test code from the provided E2E scenarios.

Task Objective:
Convert the test scenarios into actual, runnable Playwright test code, prioritizing the P0 scenarios we established. Replace the `pass` and `NotImplementedError` placeholders in our existing skeleton files.

Project Context:
- Target Application: https://demo.playwright.dev/todomvc/
- Existing Scenarios File: week4-e2e-webtest/ai-workflow/prompt1-scenarios.md
- Skeleton Files Location: week4-e2e-webtest/

IMPORTANT — Mandatory Tech Stack:
- Language: Python 3.12
- Test Runner: pytest
- Integration: pytest-playwright
- API: sync_playwright / Page sync
- Expected Assertions: Use `expect(locator).to_be_visible()`, `expect(locator).to_have_text()`, etc. (from `playwright.sync_api import expect`)

Implementation Requirements:
1. Implement the Page Object Model inside `week4-e2e-webtest/pages/todo_page.py`. Prioritize using stable locators: `get_by_placeholder`, `get_by_role`, `get_by_text`, or `get_by_test_id`.
2. Implement the tests inside `week4-e2e-webtest/tests/test_todo_crud.py` and `test_todo_filter.py` by calling the methods from the POM.
3. Every test MUST contain explicit assertions (e.g., verifying the task appears, verifying the item count). Do not just write a clicking flow.
4. Avoid using `page.wait_for_timeout()` or `time.sleep()`. Rely on Playwright's auto-wait capabilities.

Output Requirements:
- Write the final code directly into the local files.