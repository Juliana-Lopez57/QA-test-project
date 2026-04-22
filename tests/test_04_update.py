"""TC-04 - Full update (PUT)."""
import requests

from tests.config import BASE_URL, REQUEST_TIMEOUT
from utils.validators import validate_schema
from utils.file_reader import read_json_data  # <-- 1. Importas tu ayudante

def test_jsonplaceholder_update_post():
    url = f"{BASE_URL}/posts/1"
    
    # 2. Lees el archivo y sacas el payload específico para el PUT
    all_payloads = read_json_data("fixtures/test_data/payloads.json")
    body = all_payloads["valid_put"]
    
    # 3. Envías la petición usando ese 'body' que vino del archivo
    response = requests.put(url, json=body, timeout=REQUEST_TIMEOUT)
    
    assert response.status_code == 200
    payload = response.json()
    
    validate_schema(payload, "fixtures/schemas/post.schema.json")
    
    assert payload.get("id") == 1
    assert payload.get("title") == body["title"]
    assert payload.get("body") == body["body"]
    assert payload.get("userId") == body["userId"]
