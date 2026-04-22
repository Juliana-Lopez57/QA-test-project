import json
from jsonschema import validate

def validate_schema(instance, schema_file_path):
    # Abrir y leer el archivo JSON que tiene el esquema
    with open(schema_file_path, 'r') as file:
        schema = json.load(file)
    
    # La librería jsonschema hace la magia aquí
    validate(instance=instance, schema=schema)