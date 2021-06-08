import requests

from projects.golem_api.pages.utils import url, headers


DELETE_SUITE_ENDPOINT = '/suite/delete'
DUPLICATE_SUITE_ENDPOINT = '/suite/duplicate'
RENAME_SUITE_ENDPOINT = '/suite/rename'
RUN_SUITE_ENDPOINT = '/suite/run'
SAVE_SUITE_ENDPOINT = '/suite/save'
SAVE_SUITE_CODE_ENDPOINT = '/suite/code/save'
RENAME_SUITE_DIRECTORY_ENDPOINT = '/suite/directory/rename'
DELETE_SUITE_DIRECTORY_ENDPOINT = '/suite/directory/delete'


def delete_suite(project_name, suite_name, user=None):
    return requests.delete(url(DELETE_SUITE_ENDPOINT), headers=headers(user),
                           json={'project': project_name, 'fullPath': suite_name})


def duplicate_suite(project_name, suite_name, new_suite_name, user=None):
    json_ = {
        'project': project_name,
        'fullPath': suite_name,
        'newFileFullPath': new_suite_name
    }
    return requests.post(url(DUPLICATE_SUITE_ENDPOINT), headers=headers(user), json=json_)


def rename_suite(project_name, suite_name, new_suite_name, user=None):
    json_ = {
        'project': project_name,
        'fullFilename': suite_name,
        'newFullFilename': new_suite_name
    }
    return requests.post(url(RENAME_SUITE_ENDPOINT), headers=headers(user), json=json_)


def run_suite(project_name, suite_name, user=None):
    return requests.post(url(RUN_SUITE_ENDPOINT), headers=headers(user),
                         json={'project': project_name, 'suite': suite_name})


def save_suite(project_name, suite_name, tests=[], processes=1, tags=[], browsers=[],
               environments=[], user=None):
    json_ = {
        'project': project_name,
        'suite': suite_name,
        'tests': tests,
        'processes': processes,
        'tags': tags,
        'browsers': browsers,
        'environments': environments
    }
    return requests.put(url(SAVE_SUITE_ENDPOINT), headers=headers(user), json=json_)


def save_suite_code(project_name, suite_name, content, user=None):
    json_ = {
        'project': project_name,
        'suiteName': suite_name,
        'content': content
    }
    return requests.put(url(SAVE_SUITE_CODE_ENDPOINT), headers=headers(user), json=json_)


def rename_suite_directory(project_name, dir_name, new_dir_name, user=None):
    json_ = {
        'project': project_name,
        'fullDirname': dir_name,
        'newFullDirname': new_dir_name
    }
    return requests.post(url(RENAME_SUITE_DIRECTORY_ENDPOINT), headers=headers(user), json=json_)


def delete_suite_directory(project_name, dir_name, user=None):
    return requests.delete(url(DELETE_SUITE_DIRECTORY_ENDPOINT), headers=headers(user),
                           json={'project': project_name, 'fullDirname': dir_name})
