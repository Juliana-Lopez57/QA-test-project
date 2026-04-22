"""TC-03 — create post (simulated POST)."""

import requests

from tests.config import BASE_URL, REQUEST_TIMEOUT
from utils.validators import validate_schema
from utils.file_reader import read_json_data  # <-- 1. Importamos el ayudante

def test_jsonplaceholder_create_post():
    """TC-03 - Create a new post (POST)"""
    url = f"{BASE_URL}/posts"
    
    # 2. Leemos TODOS los payloads del archivo
    all_payloads = read_json_data("fixtures/test_data/payloads.json")
    
    # 3. Seleccionamos solo el que necesitamos para este test
    body = all_payloads["valid_post"]
    
    # 4. Enviamos la petición (¡El resto del test queda exactamente igual!)
    response = requests.post(url, json=body, timeout=REQUEST_TIMEOUT)

    assert response.status_code == 201
    payload = response.json()

    validate_schema(payload, "fixtures/schemas/post.schema.json")

    assert payload.get("title") == body["title"]
    assert payload.get("body") == body["body"]
    assert payload.get("userId") == body["userId"]
    assert payload.get("id") == 101