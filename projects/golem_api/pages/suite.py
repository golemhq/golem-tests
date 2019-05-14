import requests

from golem import execution

from projects.golem_api.pages import utils


DELETE_SUITE_ENDPOINT = 'api/suite/delete'
DUPLICATE_SUITE_ENDPOINT = 'api/suite/duplicate'
RENAME_SUITE_ENDPOINT = 'api/suite/rename'
RUN_SUITE_ENDPOINT = 'api/suite/run'
SAVE_SUITE_ENDPOINT = 'api/suite/save'


def delete_suite_url(base_url):
    return '{}{}'.format(base_url, DELETE_SUITE_ENDPOINT)


def duplicate_suite_url(base_url):
    return '{}{}'.format(base_url, DUPLICATE_SUITE_ENDPOINT)


def run_suite_url(base_url):
    return '{}{}'.format(base_url, RUN_SUITE_ENDPOINT)


def rename_suite_url(base_url):
    return '{}{}'.format(base_url, RENAME_SUITE_ENDPOINT)


def save_suite_url(base_url):
    return '{}{}'.format(base_url, SAVE_SUITE_ENDPOINT)


def delete_suite(project_name, suite_name, user=None):
    return requests.delete(delete_suite_url(execution.data.env.url),
                           headers=utils.common_headers(user),
                           json={'project': project_name, 'fullPath': suite_name})


def duplicate_suite(project_name, suite_name, new_suite_name, user=None):
    json_ = {
        'project': project_name,
        'fullPath': suite_name,
        'newFileFullPath': new_suite_name
    }
    return requests.post(duplicate_suite_url(execution.data.env.url),
                         headers=utils.common_headers(user), json=json_)


def rename_suite(project_name, suite_name, new_suite_name, user=None):
    json_ = {
        'project': project_name,
        'fullFilename': suite_name,
        'newFullFilename': new_suite_name
    }
    return requests.post(rename_suite_url(execution.data.env.url),
                         headers=utils.common_headers(user), json=json_)


def run_suite(project_name, suite_name, user=None):
    return requests.post(run_suite_url(execution.data.env.url),
                         headers=utils.common_headers(user),
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
    return requests.put(save_suite_url(execution.data.env.url),
                        headers=utils.common_headers(user), json=json_)
