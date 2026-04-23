"""TC-02 — get a single post by id."""

import requests

from tests.config import BASE_URL, REQUEST_TIMEOUT
from utils.validators import validate_schema

def test_jsonplaceholder_posts_by_id():
    url = f"{BASE_URL}/posts/1"
    response = requests.get(url, timeout=REQUEST_TIMEOUT)

    
    assert response.status_code == 200
    payload = response.json()

    validate_schema(payload, "fixtures/schemas/post.schema.json")
    
    assert isinstance(payload, dict)
    assert payload.get("id") == 1