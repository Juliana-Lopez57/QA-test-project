# Learning Notes - Week 2: JSON Schema and Test Data

This week I improved the tests by adding schema validation and organizing the data we send to the API.

### 1. Schema Validation vs. Business Assertions
I learned that there are two levels of checks in a test:
* **Schema Validation:** Checks the structure. It verifies that a field has the correct data type (number, string, etc.) and that required fields are present. I used the `jsonschema` library and a small `validate_schema()` helper in my project (same idea as `config.py`: one place for the logic instead of repeating it in every file).
* **Business Assertions:** Checks the actual values. It verifies that the ID is exactly 1 or that the title matches what we sent.

**Why I use both:** If I only used business assertions, I would repeat a lot of type and shape checks. If I only used schemas, I would know the JSON is valid, but I would not know the API did the right thing for the case (for example, that a title was actually updated, or that a filter returns only the rows we expect).

I keep the JSON schema files under `fixtures/schemas/` (e.g. `post.schema.json`, `post_list.schema.json`, `user.schema.json`, `user_list.schema.json`).

**Example (TC-07, filtered list):** The list schema checks that every item in the array looks like a post, but a separate loop is still needed to check business logic: every `userId` in the list must match the `userId` I passed in the query. The schema alone does not prove the filter is correct.

### 2. Personal Error with the Users List (What I Learned)
I had an issue when automating the `/users` endpoint. The test failed because I tried to use the single-user schema to validate the entire list of users.
* **My mistake:** I didn't realize that the schema needs to say `type: array` for a list, and `type: object` for a single record.
* **The fix:** I corrected the JSON schema file and learned that the structural validation completely changes when the API returns multiple items.

### 3. Test Data Management
To keep the test code clean and shorter, I extracted the "body" payloads into an external file called `payloads.json`.
* I created a helper function in `utils/file_reader.py` to read this data.
* Now, if the payload structure changes, I only have to edit the JSON file without touching the actual test code.
