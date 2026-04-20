import requests

from tests.config import BASE_URL

def test_jsonplaceholder_filter_posts():
    url = f"{BASE_URL}/posts"
    user_id = 1
   
    response = requests.get(url, params={"userId": user_id}, timeout=30)
    assert response.status_code == 200
    payload = response.json()
    assert isinstance(payload, list)
   
    assert len(payload) > 0
   
    for post in payload:
        assert post.get("userId") == user_id
    