from pydantic import BaseModel


class ResourceResponseSchema(BaseModel):
    path: str
    name: str
    type: str


class OperationResponseSchema(BaseModel):
    method: str
    href: str
    templated: bool