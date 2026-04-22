"""TC-15, TC-16 - /users resource (REST extension)."""
import requests

from tests.config import BASE_URL, REQUEST_TIMEOUT
from utils.validators import validate_schema

def test_tc15_list_users():
    """TC-15: GET /users - list users."""
    url = f"{BASE_URL}/users"
    response = requests.get(url, timeout=REQUEST_TIMEOUT)
    assert response.status_code == 200
    
    data = response.json()
    
    # 1. Validación Estructural (Usa el esquema de LISTA de usuarios)
    validate_schema(data, "fixtures/schemas/user_list.schema.json")
    
    # 2. Validación de Negocio
    assert len(data) >= 1

def test_tc16_get_user_by_id():
    """TC-16: GET /users/1 - user detail."""
    url = f"{BASE_URL}/users/1"
    response = requests.get(url, timeout=REQUEST_TIMEOUT)
    assert response.status_code == 200
    
    data = response.json()
    
    # 1. Validación Estructural (Usa el esquema de UN SOLO usuario)
    validate_schema(data, "fixtures/schemas/user.schema.json")
    
    # 2. Validación de Negocio
    assert data.get("id") == 1