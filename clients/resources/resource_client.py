import allure

from clients.api_client import ApiClient
from clients.http_builder import get_http_client
from tools.routes import DiskRoutes


class ResourcesClient(ApiClient):

    @allure.step("Create folder {path}")
    def create_folder(self, path):
        return self.put(
            DiskRoutes.RESOURCES,
            params={"path": path}
        )

    @allure.step("Get resource {path}")
    def get_resource(self, path):
        return self.get(
            DiskRoutes.RESOURCES,
            params={"path": path}
        )

    @allure.step("Upload resource from {url} to {path}")
    def upload_resource(self, path, url):
        return self.post(
            DiskRoutes.UPLOAD,
            params={
                "path": path,
                "url": url
            }
        )

    @allure.step("Delete resource {path}")
    def delete_resource(self, path):
        return self.delete(
            DiskRoutes.RESOURCES,
            params={"path": path}
        )


def get_resources_client() -> ResourcesClient:
    return ResourcesClient(session=get_http_client())