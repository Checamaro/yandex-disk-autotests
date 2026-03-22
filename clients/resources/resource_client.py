import allure

from clients.api_client import ApiClient
from tools.routes import DiskRoutes


class ResourcesClient(ApiClient):

    def create_folder(self, path):

        with allure.step(f"Create folder '{path}'"):
            return self.put(
                DiskRoutes.RESOURCES,
                params={"path": path}
            )

    def get_resource(self, path):

        with allure.step(f"Get resource '{path}'"):
            return self.get(
                DiskRoutes.RESOURCES,
                params={"path": path}
            )

    def upload_resource(self, path, url):

        with allure.step(f"Upload file from '{url}' to '{path}'"):
            return self.post(
                DiskRoutes.UPLOAD,
                params={
                    "path": path,
                    "url": url
                }
            )

    def delete_resource(self, path):

        with allure.step(f"Delete resource '{path}'"):
            return self.delete(
                DiskRoutes.RESOURCES,
                params={"path": path}
            )