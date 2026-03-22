import allure

from clients.api_client import ApiClient
from tools.routes import DiskRoutes


class DiskClient(ApiClient):

    def get_disk_info(self):

        with allure.step("Get disk information"):
            return self.get(DiskRoutes.DISK_INFO)

