import pytest
import allure
from tools.fakers import random_folder


@pytest.fixture
def folder_name():
    with allure.step("Generate random folder name"):
        return random_folder()


@pytest.fixture
def long_folder_name():
    with allure.step("Generate long folder name"):
        return "a" * 256
