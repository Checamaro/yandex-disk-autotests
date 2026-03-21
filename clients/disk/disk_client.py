from clients.api_client import ApiClient
from tools.enums.routes import DiskRoutes


class DiskClient(ApiClient):

    def get_disk_info(self):
        return self.get(DiskRoutes.DISK_INFO)

    def create_folder(self, path):
        return self.put(
            DiskRoutes.RESOURCES,
            params={"path": path}
        )

    def get_resource(self, path):
        return self.get(
            DiskRoutes.RESOURCES,
            params={"path": path}
        )

    def upload_resource(self, path, url):
        return self.post(
            DiskRoutes.UPLOAD,
            params={
                "path": path,
                "url": url
            }
        )

    def delete_resource(self, path):
        return self.delete(
            DiskRoutes.RESOURCES,
            params={"path": path}
        )
