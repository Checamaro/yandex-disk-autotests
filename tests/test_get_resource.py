import allure
from tools.assertions.disk import DiskAssertions


@allure.feature("Resources")
def test_get_resource(disk_client, folder_name):
    disk_client.create_folder(folder_name)
    r = disk_client.get_resource(folder_name)

    DiskAssertions.resource(r)
