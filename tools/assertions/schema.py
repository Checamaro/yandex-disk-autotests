def validate_schema(response, schema):
    schema(**response.json())
