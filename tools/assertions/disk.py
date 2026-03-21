from tools.assertions.base import assert_status
from tools.assertions.schema import validate_schema

from clients.disk.disk_schema import (
    DiskInfo,
    ResourceResponse,
    OperationResponse
)


class DiskAssertions:

    @staticmethod
    def disk_info(response):
        assert_status(response, 200)

        validate_schema(response, DiskInfo)

    @staticmethod
    def folder_created(response):
        assert_status(response, 201)

        validate_schema(response, OperationResponse)

    @staticmethod
    def resource(response):
        assert_status(response, 200)

        validate_schema(response, ResourceResponse)

    @staticmethod
    def upload_started(response):
        assert_status(response, 202)

        validate_schema(response, OperationResponse)

    @staticmethod
    def deleted(response):
        assert_status(response, 204)
