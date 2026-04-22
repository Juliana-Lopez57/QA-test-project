"""TC-06 — delete post (simulated DELETE)."""

import requests

from tests.config import BASE_URL, REQUEST_TIMEOUT


def test_jsonplaceholder_delete_post():
    url = f"{BASE_URL}/posts/1"
    response = requests.delete(url, timeout=REQUEST_TIMEOUT)
    
    assert response.status_code == 200

    payload = response.json()
    assert isinstance(payload, dict)
    assert len(payload) == 0

 
