Act as a QA E2E Expert and Playwright automation engineer. Generate a Playwright test skeleton for this project based on the selected E2E scenarios provided in prompt1-scenarios.md.

Task Objective:
Based on the existing test scenarios, generate an extensible and maintainable Playwright test skeleton. Do not write the full assertions or interaction details yet; just establish the correct architecture.

Project Context:
- Target Application: https://demo.playwright.dev/todomvc/
- Existing Scenarios File: week4-e2e-webtest/ai-workflow/prompt1-scenarios.md

IMPORTANT — Mandatory Tech Stack:
- Language: Python 3.12
- Test Runner: pytest
- Integration: pytest-playwright
- API: sync_playwright / Page sync
- DO NOT generate TypeScript/JavaScript. DO NOT generate *.spec.ts files.

Execution Requirements:
Create the skeleton for the following structure:
1. `week4-e2e-webtest/tests/conftest.py`: (pytest configuration)
2. `week4-e2e-webtest/pages/todo_page.py`: (Page Object Model class with empty methods/TODOs for the actions we need)
3. `week4-e2e-webtest/tests/test_todo_crud.py`: (Test file with the test function names mapping to our 4 critical journeys, using `pass` for now).

Output Requirements:
- Save all generated skeleton code directly to the local files mentioned above.