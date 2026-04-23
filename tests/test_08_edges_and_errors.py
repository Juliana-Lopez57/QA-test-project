"""TC-08, TC-09, TC-10, TC-12, TC-13, TC-14 — edges, errors, and security-style checks (mock)."""

import requests
from tests.config import BASE_URL, REQUEST_TIMEOUT
from utils.validators import validate_schema

def test_tc08_post_with_boundary_user_id():
    """TC-08: POST /posts with boundary userId (10) - expect 201."""
    url = f"{BASE_URL}/posts"
    body = {
        "title": "Boundary user",
        "body": "Body",
        "userId": 10,
    }
    response = requests.post(url, json=body, timeout=REQUEST_TIMEOUT)
    assert response.status_code == 201
    
    data = response.json()
    validate_schema(data, "fixtures/schemas/post.schema.json")
    assert data.get("userId") == 10

def test_tc09_post_with_empty_title():
    """TC-09: POST /posts with empty title - mock usually accepts (201)."""
    url = f"{BASE_URL}/posts"
    body = {
        "title": "",
        "body": "Body with empty title case",
        "userId": 1,
    }
    response = requests.post(url, json=body, timeout=REQUEST_TIMEOUT)
    assert response.status_code == 201
    
    data = response.json()
    validate_schema(data, "fixtures/schemas/post.schema.json")
    assert data.get("title") == ""

def test_tc10_get_post_with_non_numeric_id_returns_404():
    """TC-10: GET /posts/abc - non-numeric id -> 404."""
    url = f"{BASE_URL}/posts/abc"
    response = requests.get(url, timeout=REQUEST_TIMEOUT)
    
    assert response.status_code == 404

def test_tc12_get_nonexistent_post_returns_404():
    """TC-12: GET /posts/55555 - non-existent resource -> 404."""
    url = f"{BASE_URL}/posts/55555"
    response = requests.get(url, timeout=REQUEST_TIMEOUT)
    
    assert response.status_code == 404

def test_tc13_post_malformed_json_returns_500_on_mock():
    """TC-13: invalid JSON - this mock often returns 500 instead of 400."""
    url = f"{BASE_URL}/posts"
    response = requests.post(
        url,
        data="{not valid json",
        headers={"Content-Type": "application/json"},
        timeout=REQUEST_TIMEOUT,
    )
    
    assert response.status_code == 500

def test_tc14_post_with_script_in_title_is_echoed():
    """TC-14: injection-like string in title - document reflection in mock (201)."""
    url = f"{BASE_URL}/posts"
    malicious_title = "<script>alert(1)</script>"
    body = {
        "title": malicious_title,
        "body": "Security documentation case",
        "userId": 1,
    }
    response = requests.post(url, json=body, timeout=REQUEST_TIMEOUT)
    assert response.status_code == 201
    
    data = response.json()
    validate_schema(data, "fixtures/schemas/post.schema.json")
    assert data.get("title") == malicious_title