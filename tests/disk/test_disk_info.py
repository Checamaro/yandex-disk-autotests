import pytest
import allure
from tools.assertions.disk import DiskAssertions
from allure_commons.types import Severity


@pytest.mark.disk
@pytest.mark.regression
@allure.feature("Disk")
@allure.parent_suite("Yandex Disk")
@allure.suite("Disk")
class TestDisk:

    @allure.story("Get disk info")
    @allure.title("Get disk info")
    @allure.severity(Severity.CRITICAL)
    def test_disk_info(self, disk_client):
        r = disk_client.get_disk_info()

        DiskAssertions.disk_info(r)