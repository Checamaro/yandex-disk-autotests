import pytest
from clients.resources.resource_client import ResourcesClient


@pytest.fixture
def resources_client():
    return ResourcesClient()