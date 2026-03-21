import allure
from tools.assertions.disk import DiskAssertions


@allure.feature("Disk")
def test_disk_info(disk_client):
    r = disk_client.get_disk_info()

    DiskAssertions.disk_info(r)
