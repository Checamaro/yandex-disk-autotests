from pydantic import BaseModel


class DiskInfo(BaseModel):
    total_space: int
    used_space: int



