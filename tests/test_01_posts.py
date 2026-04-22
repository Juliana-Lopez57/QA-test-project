"""TC-01 — list all posts."""

import requests

from tests.config import BASE_URL, REQUEST_TIMEOUT
from utils.validators import validate_schema


def test_jsonplaceholder_posts():
    url = f"{BASE_URL}/posts"
    response = requests.get(url, timeout=REQUEST_TIMEOUT)
    
    assert response.status_code == 200
    payload = response.json()

    validate_schema(payload, "fixtures/schemas/post_list.schema.json")
  
    assert isinstance(payload, list)
    assert len(payload) > 0
