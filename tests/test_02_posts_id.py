import requests

from tests.config import BASE_URL


def test_jsonplaceholder_posts_by_id():
    url = f"{BASE_URL}/posts/1"
    response = requests.get(url, timeout=30)

    assert response.status_code == 200
    payload = response.json()

    assert isinstance(payload, dict)
    assert payload.get("id") == 1

    assert "title" in payload
    assert "body" in payload
    assert "userId" in payload
