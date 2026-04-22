"""TC-07 - filter posts by userId."""
import requests

from tests.config import BASE_URL, REQUEST_TIMEOUT
from utils.validators import validate_schema

def test_jsonplaceholder_filter_posts():
    url = f"{BASE_URL}/posts"
    user_id = 1
    
    
    response = requests.get(url, params={"userId": user_id}, timeout=REQUEST_TIMEOUT)
    
   
    assert response.status_code == 200
    payload = response.json()
    
    
    validate_schema(payload, "fixtures/schemas/post_list.schema.json")
    
    
    assert len(payload) > 0
   
    for post in payload:
        assert post.get("userId") == user_id
    