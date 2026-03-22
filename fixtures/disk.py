import pytest

from clients.disk.disk_client import get_disk_client


@pytest.fixture
def disk_client():
    return get_disk_client()