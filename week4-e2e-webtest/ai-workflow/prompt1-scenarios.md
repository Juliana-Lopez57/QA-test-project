Use `@testing-qa` and `@test-automator` to analyze this web application and generate high-value end-to-end test scenarios based on its UI and functionality.

Task Objective: Extract executable, traceable, and suitable E2E test scenarios for future Playwright implementation based on the public web application.

Project Context:
- Target URL: https://demo.playwright.dev/todomvc/
- Technology Stack: Frontend Web App (Vanilla JS/React)
- Authentication Method: None (Public access)
- Output Language: English
- Generate only test scenarios, not test code
- Scenario Output File: week4-e2e-webtest/ai-workflow/prompt1-scenarios.md

Please focus on analyzing the features available at the URL:
- Task creation input field
- Task list behavior (edit, delete, mark as complete)
- Filters (All, Active, Completed)
- Items left counter
- Clear completed button

Analysis Requirements:
1. Identify Page Preconditions:
- Empty state vs. populated state
2. Identify Key User Actions:
- Add a task
- Complete a task
- Delete a task
- Filter tasks
- Clear completed
3. Identify Branches and Exceptions:
- Empty task submission
- Edge cases (e.g., hiding filters if there are no tasks)
4. Do not create unnecessary features.
5. Save the final result locally to `week4-e2e-webtest/ai-workflow/prompt1-scenarios.md` in Markdown format.

The output format must strictly adhere to the following:

# Application Overview
- Main Pages:
- Main Protected Pages:
- Main High-Risk Business Points:
- Recommended Priority Coverage Modules:

# Page-Level E2E Test Scenarios

## Page: TodoMVC Home
- URL: https://demo.playwright.dev/todomvc/
- Preconditions:
- Critical Dependencies:
- Suggested Priority: P0 / P1 / P2

### Scenario 1: <Title>
- Type: Access Control / Success Path / Validation / Branch / Exception / Regression
- Preconditions:
- Operation Steps:
- Expected Result:
- Test Data Requirements:

### Scenario 2: <Title>
(Continue with other scenarios...)

# Missing Information/Items to be Confirmed
- Project:
- Impact:

Supplementary Requirements:
- For each page with a form (input), consider at least:
  - Required field validation (empty input)
  - Successful submission
- Do not write Playwright code; only output test scenarios.
- Finally, in addition to displaying a summary in the dialog, the complete result must also be written to `week4-e2e-webtest/ai-workflow/prompt1-scenarios.md`.

# Human Review: Selected Critical User Journeys (P0)
Based on the AI-generated scenarios, the following 4 critical End-to-End journeys have been selected for Playwright automation:

### Journey 1: Core Task Creation and Default State
- Goal: Verify that a user can add a new task and it appears correctly.

### Journey 2: Task Completion and Counter Accuracy
- Goal: Verify that marking a task as complete updates the UI and counter.

### Journey 3: Routing and Filtering
- Goal: Verify that the Active and Completed filters display the correct tasks.

### Journey 4: Destructive Action - Clear Completed
- Goal: Verify that users can bulk-delete completed tasks.