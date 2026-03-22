from pydantic import BaseModel


class DiskInfoSchema(BaseModel):
    total_space: int
    used_space: int



