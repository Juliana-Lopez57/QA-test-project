"""TC-05 — partial update (PATCH)."""

import requests

from tests.config import BASE_URL, REQUEST_TIMEOUT
from utils.validators import validate_schema


def test_jsonplaceholder_partial_update_post():
    url = f"{BASE_URL}/posts/1"
    body = {
        "title": "Patched title only"
        }
    
    response = requests.patch(url, json=body, timeout=REQUEST_TIMEOUT)
    
    assert response.status_code == 200
    payload = response.json()
    
    validate_schema(payload, "fixtures/schemas/post.schema.json")
    
    assert payload.get("id") == 1
    assert payload.get("title") == body["title"]
    
