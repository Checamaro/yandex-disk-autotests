import allure

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

        with allure.step("Check disk info response"):
            assert_status(response, 200)
            validate_schema(response, DiskInfo)

    @staticmethod
    def folder_created(response):

        with allure.step("Check folder created"):
            assert_status(response, 201)
            validate_schema(response, OperationResponse)

    @staticmethod
    def resource(response):

        with allure.step("Check resource metadata"):
            assert_status(response, 200)
            validate_schema(response, ResourceResponse)

    @staticmethod
    def upload_started(response):

        with allure.step("Check upload started"):
            assert_status(response, 202)
            validate_schema(response, OperationResponse)

    @staticmethod
    def deleted(response):

        with allure.step("Check resource deleted"):
            assert_status(response, 204)