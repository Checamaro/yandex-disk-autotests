import pytest
import allure

from tools.assertions.disk import DiskAssertions
from tools.fakers import random_folder
from clients.errors_schema import ErrorResponse
from allure_commons.types import Severity


@pytest.mark.resources
@pytest.mark.regression
@allure.feature("Resources")
@allure.parent_suite("Yandex Disk")
@allure.suite("Resources")
class TestResources:

    @allure.story("Create folder")
    @allure.title("Create folder positive")
    @allure.severity(Severity.BLOCKER)
    @pytest.mark.parametrize(
        "folder_name",
        [
            lambda: random_folder(),
            lambda: random_folder(),
        ]
    )
    def test_create_folder_positive(self, disk_client, folder_name):
        """Позитивное создание папки"""

        if callable(folder_name):
            folder_name = folder_name()

        r = disk_client.create_folder(folder_name)

        DiskAssertions.folder_created(r)

    @allure.story("Create folder")
    @allure.title("Create folder negative")
    @allure.severity(Severity.NORMAL)
    @pytest.mark.parametrize(
        "folder_name, expected_status",
        [
            ("", 400),
            ("/" + "a" * 256, 404),
            ("existing_folder", 409),
        ]
    )
    def test_create_folder_negative(self, disk_client, folder_name, expected_status):
        """Негативные сценарии создания папки"""

        if folder_name == "existing_folder":
            disk_client.create_folder(folder_name)

        r = disk_client.create_folder(folder_name)

        assert r.status_code == expected_status

        if r.status_code != 201:
            ErrorResponse(**r.json())

    @allure.story("Get resource")
    @allure.title("Get folder metadata")
    @allure.severity(Severity.CRITICAL)
    def test_get_resource(self, disk_client, folder_name):
        """Получение информации о папке"""

        disk_client.create_folder(folder_name)

        r = disk_client.get_resource(folder_name)

        DiskAssertions.resource(r)

    @allure.story("Upload resource")
    @allure.title("Upload resource from URL")
    @allure.severity(Severity.CRITICAL)
    def test_upload_resource(self, disk_client, folder_name):
        """Загрузка файла по URL"""

        disk_client.create_folder(folder_name)

        r = disk_client.upload_resource(
            path=folder_name,
            url="http://example.com"
        )

        DiskAssertions.upload_started(r)

    @allure.story("Delete resource")
    @allure.title("Delete folder")
    @allure.severity(Severity.CRITICAL)
    def test_delete_resource(self, disk_client, folder_name):
        """Удаление папки"""

        disk_client.create_folder(folder_name)

        r = disk_client.delete_resource(folder_name)

        DiskAssertions.deleted(r)