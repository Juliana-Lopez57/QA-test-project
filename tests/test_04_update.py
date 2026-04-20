import requests

from tests.config import BASE_URL

def test_jsonplaceholder_update_post():
    url = f"{BASE_URL}/posts/1"
    body = {
        "id": 1,
        "title": "Updated title",
        "body": "Updated body",
        "userId": 1,
    }
    response = requests.put(url, json=body, timeout=30)
    assert response.status_code == 200
    
    payload = response.json()
    assert isinstance(payload, dict)
    
    assert payload.get("id") == 1
    assert payload.get("title") == body["title"]
    assert payload.get("body") == body["body"]
    assert payload.get("userId") == body["userId"]
