import allure
from tools.assertions.disk import DiskAssertions


@allure.feature("Resources")
def test_delete_resource(disk_client, folder_name):
    disk_client.create_folder(folder_name)
    r = disk_client.delete_resource(folder_name)

    DiskAssertions.deleted(r)
