import allure

from tools.assertions.base import assert_status
from tools.assertions.schema import validate_schema

from clients.resources.resource_schema import ResourceResponseSchema, OperationResponseSchema


class ResourcesAssertions:

    @staticmethod
    def folder_created(response):
        with allure.step("Check folder created"):
            assert_status(response, 201)
            validate_schema(response, OperationResponseSchema)

    @staticmethod
    def resource(response):
        with allure.step("Check resource metadata"):
            assert_status(response, 200)
            validate_schema(response, ResourceResponseSchema)

    @staticmethod
    def upload_started(response):
        with allure.step("Check upload started"):
            assert_status(response, 202)
            validate_schema(response, OperationResponseSchema)

    @staticmethod
    def deleted(response):
        with allure.step("Check resource deleted"):
            assert_status(response, 204)
