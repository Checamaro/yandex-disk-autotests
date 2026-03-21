from pydantic import BaseModel


class DiskInfo(BaseModel):
    total_space: int
    used_space: int


class ResourceResponse(BaseModel):
    path: str
    name: str
    type: str


class OperationResponse(BaseModel):
    method: str
    href: str
    templated: bool
