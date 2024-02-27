import os
import json


def load_schema(filename: str):
    schema_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname((os.path.abspath(__file__))))),
                               'schema', filename)
    with open(schema_path) as file:
        schema = json.load(file)
        return schema
