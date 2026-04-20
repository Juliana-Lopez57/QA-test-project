import requests

from tests.config import BASE_URL

def test_jsonplaceholder_delete_post():
    
    url = f"{BASE_URL}/posts/1"
    response = requests.delete(url, timeout=30)
    
    assert response.status_code == 200

    payload = response.json()
    assert isinstance(payload, dict)
    assert len(payload) == 0

 
