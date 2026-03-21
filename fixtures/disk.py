import pytest
from clients.disk.disk_client import DiskClient


@pytest.fixture
def disk_client():
    return DiskClient()
