import pytest
from tools.fakers import random_folder


@pytest.fixture
def folder_name():
    return random_folder()

@pytest.fixture
def long_folder_name():
    return "a" * 256