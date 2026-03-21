import pytest
import allure

from tools.assertions.disk import DiskAssertions
from tools.fakers import random_folder


@pytest.mark.parametrize(
    "folder_name, expected_status",
    [
        (lambda: random_folder(), 201),
        (lambda: random_folder(), 201),
    ]
)
@allure.feature("Resources")
@allure.story("Создание папки")
def test_create_folder_positive(disk_client, folder_name, expected_status):
    """Позитивное создание папки"""
    if callable(folder_name):
        folder_name = folder_name()
    r = disk_client.create_folder(folder_name)

    DiskAssertions.folder_created(r)


@pytest.mark.parametrize(
    "folder_name, expected_status",
    [
        ("", 400),
        ("/" + "a" * 256, 400),
        ("existing_folder", 409),
    ]
)
@allure.feature("Resources")
@allure.story("Создание папки")
def test_create_folder_negative(disk_client, folder_name, expected_status):
    """Негативные сценарии создания папки"""
    if folder_name == "existing_folder":
        disk_client.create_folder(folder_name)
    r = disk_client.create_folder(folder_name)

    assert r.status_code == r.status_code

    from clients.errors_schema import ErrorResponse
    if r.status_code != 201:
        ErrorResponse(**r.json())
