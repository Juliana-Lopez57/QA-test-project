---
name: jsonplaceholder-api
description: >-
  Beginner-friendly knowledge base for pytest API automation in QA-TEST-PROJECT against
  JSONPlaceholder. Simple, readable tests for Junior QA moving from manual testing; REST
  basics, TC-01–TC-14 matrix, mock quirks, 20+ cases target, and mentorship guardrails.
  Use when working on API tests, jsonplaceholder.typicode.com, test matrices, TC-XX IDs,
  pytest suite completion, or Phase 1 of the General QA upskilling plan.
---

# JSONPlaceholder API testing — knowledge base (Junior QA)

## 1. Project context and goal

- **Repo:** `QA-TEST-PROJECT`; tests live under `tests/`.
- **API:** `https://jsonplaceholder.typicode.com` (public REST mock).
- **Goal:** Learn API automation with **simple, linear, easy-to-read** code — like manual steps turned into Python.
- **Base URL:** Import `BASE_URL` from `tests.config` (do not scatter the host string across tests).
- **Stack:** `pytest` + `requests`. Use **`timeout=30`** on every HTTP call (or a constant such as `REQUEST_TIMEOUT` in `tests.config`) so tests do not hang.
- **Learning plan:** General QA upskilling, Phase 1 (weeks 1–2): API scenarios + automation. JSON Schema, CI, and reporting are later phases — out of scope unless the user asks.

---

## 2. Coding style (keep it simple)

- **No advanced pytest magic:** Avoid complex fixtures, `conftest.py`, abstract classes, or heavy decorators unless the user explicitly wants to level up. Prefer **explicit** code.
- **One test = one function:** Prefer separate test functions for different scenarios instead of large `@pytest.mark.parametrize` blocks. Parametrize is OK when it is a **small** set of variations of the **same** flow (e.g. two `userId` values) and each row stays easy to read.
- **Explicit steps** (mirror manual cases):

  1. Build URL and payload (if any).
  2. Send the request (with `timeout`).
  3. Assert status code.
  4. Assert response body (shape and fields that matter).

- **Educational comments:** Add short comments on **steps and non-obvious checks** (e.g. why the mock returns 500). Do not comment every import or trivial `assert response.status_code == 200`.
- **Independence:** No shared mutable state between tests; each test must pass alone and in any order.

---

## 3. Basic assertions (enough is enough)

Keep asserts straightforward:

- `assert response.status_code == 200`
- `assert "id" in data`
- `assert data["userId"] == 1`

For mock-generated `id` values, prefer **presence + type** over a fixed number unless the case explicitly pins behavior. Do not assert only status with no body checks.

---

## 4. JSONPlaceholder quirks (encode these in tests)

- **POST/PUT/PATCH:** Simulated — often **201** (POST) or **200** with echoed data; nothing is really persisted. Assert echoed fields and that an `id` exists as documented below.
- **Client-sent `id` in POST** may be ignored or normalized; assert the server returns an `id`, not necessarily the value you sent.
- **Malformed JSON** usually returns **500** on this mock, not 400 — expect that.
- **Bad or non-numeric IDs** (e.g. `/posts/abc`, or non-existent ids like `/posts/99999`): **404**.
- **TC-11 (POST without JSON Content-Type):** behavior can vary (e.g. 200 / 201 / 400). **Document what the live API returns** in the test or comment; do not invent a single code without checking.
- **Injection-style strings** in title/body: often echoed unchanged — treat as **documentation** of mock behavior, not proof of security controls.

---

## 5. Canonical matrix (TC-01 – TC-14)

Baseline: every ID should map to at least one automated test, or be marked out of scope with a reason.

**Do not rename, skip, or renumber TC-01–TC-14** without team agreement — keep matrix, code, and any Excel sheet aligned.

| ID | Category | Summary | Method | Path / notes | Expected status |
|----|----------|---------|--------|--------------|-----------------|
| TC-01 | Happy path | List posts | GET | `/posts` | 200, array length ≥ 1 |
| TC-02 | Happy path | Get existing post | GET | `/posts/1` | 200, object with `id`, `userId`, `title`, `body` |
| TC-03 | Happy path | Create post | POST | `/posts` | 201, echoed fields, `id` present |
| TC-04 | Happy path | Full update | PUT | `/posts/1` | 200, echoed body |
| TC-05 | Happy path | Partial update | PATCH | `/posts/1` | 200, patched fields reflected |
| TC-06 | Happy path | Delete post | DELETE | `/posts/1` | 200, often `{}` |
| TC-07 | Happy path | Filter by userId | GET | `/posts?userId=1` | 200, every item `userId == 1` |
| TC-08 | Edge | Boundary userId | POST | `/posts` with `userId: 10` | 201 |
| TC-09 | Edge | Empty title | POST | `title: ""` | 201 |
| TC-10 | Edge | Non-numeric id | GET | `/posts/abc` | 404 |
| TC-11 | Edge | POST without JSON Content-Type | POST | raw text body | document observed behavior |
| TC-12 | Error | Non-existent post | GET | `/posts/88888` | 404 |
| TC-13 | Error | Malformed JSON | POST | invalid JSON string | 400 or 500 (mock often 500) |
| TC-14 | Security | Injection in title/body | POST | `<script>…</script>` | 201, value echoed unchanged |

---

## 6. Target suite size and extensions

- **Minimum:** **20** automated cases — TC-01–TC-14 plus at least **6** extensions (TC-15+).
- **Recommended:** **25** for a bit more practice and review.
- When proposing **TC-15+**, use a simple table: **Case ID, Title, Endpoint, Method, Expected Status, Priority, Expected risk / what we prove.**
- Good extension ideas: `/users`, `/users/1`, `/posts/1/comments`, `?postId=1`, `_limit` / `_page` if useful, GET `/posts/0`, filters that return an empty list, unsupported method on a resource — keep scenarios **easy to explain** to a beginner.
- **Counting:** If one parametrized test covers N distinct scenarios, document sub-IDs (e.g. TC-16a, TC-16b) where the team tracks the matrix.
- If adding **more than two** new cases at once, you may propose the table first, then implement — unless the user asks to implement directly.

---

## 7. Test data and files

- Shared constants stay in **`tests/config.py`** (e.g. `BASE_URL`, optional timeout constant).
- Reusable payloads can live in a small **`tests/data.py`** or clearly named dicts — avoid copy-pasting the same payload everywhere.
- Prefer **one area per file** when the suite grows (e.g. create, read, update, delete, filter, errors) — names should stay readable.

---

## 8. AI guardrails and mentorship

- Act as a **patient mentor**: code should be readable for someone new to Python and pytest.
- **Complete files only** when generating Python — never `# ... rest of code` or omitted blocks.
- When behavior is unclear, **state the assumption** and suggest verifying against the live API or Postman before locking an assertion.
- After generating code or new scenarios, end with **one** concrete check-in, for example: *¿Te queda claro este test? Si quieres, te explico línea por línea o revisamos un caso borde que no hayamos cubierto.* (Or the same idea in English if the user prefers.)

---

## 9. When this skill applies

Use when: designing or extending the suite, mapping matrix rows to tests, naming cases, explaining JSONPlaceholder behavior, proposing TC-15+ rows, or keeping tests simple and teachable.
