import json
from jsonschema import validate

def validate_schema(instance, schema_file_path):
    
    with open(schema_file_path, 'r') as file:
        schema = json.load(file)
    
    
    validate(instance=instance, schema=schema)