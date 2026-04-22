"""TC-02 — get a single post by id."""

import requests

from tests.config import BASE_URL, REQUEST_TIMEOUT
from utils.validators import validate_schema

def test_jsonplaceholder_posts_by_id():
    url = f"{BASE_URL}/posts/1"
    response = requests.get(url, timeout=REQUEST_TIMEOUT)

    # 1. Validate HTTP status code
    assert response.status_code == 200
    payload = response.json()

    # 2. Structural validation with JSON Schema
    # This replaces your old "title in payload" asserts
    validate_schema(payload, "fixtures/schemas/post.schema.json")

    # 3. Business validation
    assert isinstance(payload, dict)
    assert payload.get("id") == 1