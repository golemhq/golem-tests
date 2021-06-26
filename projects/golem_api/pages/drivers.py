import requests

from projects.golem_api.pages.utils import url, headers


DRIVERS_FILES_ENDPOINT = '/drivers/files'
DELETE_DRIVER_ENDPOINT = '/drivers/delete'
UPDATE_DRIVER_ENDPOINT = '/drivers/update'


def get_driver_files(user=None):
    return requests.get(url(DRIVERS_FILES_ENDPOINT), headers=headers(user))


def delete_driver(filename, user=None):
    return requests.delete(url(DELETE_DRIVER_ENDPOINT), headers=headers(user),
                           json={'filename': filename})


def update_driver(driver_name, user=None):
    return requests.post(url(UPDATE_DRIVER_ENDPOINT), headers=headers(user),
                         json={'driverName': driver_name})