import allure

from clients.api_client import ApiClient
from clients.http_builder import get_http_client
from tools.routes import DiskRoutes


class DiskClient(ApiClient):

    @allure.step("Get disk information")
    def get_disk_info(self):
        return self.get(DiskRoutes.DISK_INFO)


def get_disk_client() -> DiskClient:
    with allure.step("Create Disk API client"):
        return DiskClient(session=get_http_client())