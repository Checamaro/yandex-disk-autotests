import allure

from tools.assertions.base import assert_status
from tools.assertions.schema import validate_schema

from clients.disk.disk_schema import DiskInfoSchema


class DiskAssertions:

    @staticmethod
    def disk_info(response):

        with allure.step("Check disk info response"):
            assert_status(response, 200)
            validate_schema(response, DiskInfoSchema)

