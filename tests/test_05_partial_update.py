import requests

from tests.config import BASE_URL

def test_jsonplaceholder_partial_update_post():
    url = f"{BASE_URL}/posts/1"
    body = {
        "title": "Patched title only"
        }
    
    response = requests.patch(url, json=body, timeout=30)
    
    assert response.status_code == 200
    payload = response.json()
    assert isinstance(payload, dict)
    
    assert payload.get("id") == 1
    assert payload.get("title") == body["title"]
    
