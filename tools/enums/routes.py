from enum import Enum


class DiskRoutes(str, Enum):
    DISK_INFO = "/v1/disk"

    RESOURCES = "/v1/disk/resources"

    UPLOAD = "/v1/disk/resources/upload"
