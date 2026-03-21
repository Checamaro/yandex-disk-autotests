import allure
from tools.assertions.disk import DiskAssertions


@allure.feature("Upload")
def test_upload_resource(disk_client, folder_name):
    disk_client.create_folder(folder_name)

    r = disk_client.upload_resource(
        path=folder_name,
        url="http://example.com"
    )

    DiskAssertions.upload_started(r)
