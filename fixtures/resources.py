import pytest

from clients.resources.resource_client import get_resources_client


@pytest.fixture
def resources_client():
    return get_resources_client()