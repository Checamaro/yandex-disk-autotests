from pydantic import BaseModel


class ResourceResponse(BaseModel):
    path: str
    name: str
    type: str


class OperationResponse(BaseModel):
    method: str
    href: str
    templated: bool