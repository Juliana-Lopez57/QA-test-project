# Learning Notes - Week 1: API Automation Foundation

In this first week, I moved my manual Postman test cases to code using Python with the `pytest` and `requests` libraries. I automated scenarios from the test matrix (TC-01 through TC-14, plus a few extra cases).

### 1. Pytest and Requests Basics
* I learned how to organize tests into independent functions inside `.py` files.
* Each test can run on its own and in any order. I avoided chaining steps that would depend on another test’s data.
* I used a `config.py` file to avoid repeating the base URL and timeout in every test. This makes the code much easier to maintain.
* I run the suite with `pytest` from the **project root** so paths to config and fixtures resolve correctly.

### 2. HTTP Methods and Validations
* I wrote tests for GET, POST, PUT, PATCH, and DELETE requests.
* In each test, I first verify the status code (like 200 or 201) and then check the expected JSON content using `response.json()`.

### 3. API Mock Behavior
* I understood that JSONPlaceholder is a mock system. For example, when creating a new post, it always returns ID 101, which I have to account for in my assertions.
* POST, PUT, PATCH, and DELETE return success and often echo the request body in the response, but **nothing is really persisted** in a database. That is why the mock can look “stable” in demos and why new posts always get the same fake new ID.
* I also tested error cases, like requesting a non-existent ID (404) or sending malformed JSON (500), to see how the system handles bad inputs.
