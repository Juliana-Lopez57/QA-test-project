import requests

from tests.config import BASE_URL

def test_jsonplaceholder_posts():
    
    url = f"{BASE_URL}/posts"
    response = requests.get(url, timeout=30)
    
    assert response.status_code == 200
    payload = response.json()
  
    assert isinstance(payload, list)
    assert len(payload) > 0
