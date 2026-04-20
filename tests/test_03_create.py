import requests

from tests.config import BASE_URL

def test_jsonplaceholder_create_post():
    url = f"{BASE_URL}/posts"
    body = {
        "title": "Test title",
        "body": "Test body",
        "userId": 1,
    }
    response = requests.post(url, json=body, timeout=30)

    assert response.status_code == 201
    
    payload = response.json()
    assert isinstance(payload, dict)
    
    assert "id" in payload
    assert isinstance(payload["id"], int)
    
    assert payload.get("title") == body["title"]
    assert payload.get("body") == body["body"]
    assert payload.get("userId") == body["userId"]
