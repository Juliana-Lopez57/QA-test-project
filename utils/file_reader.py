import json

def read_json_data(file_path):
    """Reads a JSON file and returns its content as a Python dictionary."""
    with open(file_path, 'r') as file:
        return json.load(file)