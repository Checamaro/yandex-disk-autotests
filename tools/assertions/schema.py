def validate_schema(response, schema):
    schema.model_validate(response.json())