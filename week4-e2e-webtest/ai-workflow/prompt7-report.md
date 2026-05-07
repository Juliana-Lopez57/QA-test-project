Act as a QA E2E Expert. Run the Playwright tests and generate an integration test report based on the real terminal output.

Task Objective:
Execute the tests in the terminal, capture the real results, and write a Markdown report. Do not claim tests passed without real verification.

Project Context:
- Project Path: week4-e2e-webtest/
- Test Command: `pytest week4-e2e-webtest/tests -v`
- Report Output File: week4-e2e-webtest/reports/latest-report.md

Execution Steps:
1. Run the test command provided above in the terminal.
2. Read and summarize the real output.
3. Generate a test report in Markdown format.
4. Save the full report locally to `week4-e2e-webtest/reports/latest-report.md` (create the `reports` directory if it does not exist).

Report Format Requirements:
# Integration Test Report
## 1. Execution Summary
- Execution Time:
- Test Command Used:
- Overall Conclusion: Passed / Failed

## 2. Test Statistics
- Total Cases:
- Passed:
- Failed:
- Skipped:

## 3. Execution Details
(Briefly list the tests that ran and their status based on the terminal output)