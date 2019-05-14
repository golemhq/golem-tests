import requests

from golem import execution

from projects.golem_api.pages import utils


DELETE_TEST_ENDPOINT = 'api/test/delete'
DUPLICATE_TEST_ENDPOINT = 'api/test/duplicate'
RENAME_TEST_ENDPOINT = 'api/test/rename'
RUN_TEST_ENDPOINT = 'api/test/run'
SAVE_TEST_ENDPOINT = 'api/test/save'
SAVE_TEST_CODE_ENDPOINT = 'api/test/code/save'


def delete_test_url(base_url):
    return '{}{}'.format(base_url, DELETE_TEST_ENDPOINT)


def duplicate_test_url(base_url):
    return '{}{}'.format(base_url, DUPLICATE_TEST_ENDPOINT)


def run_test_url(base_url):
    return '{}{}'.format(base_url, RUN_TEST_ENDPOINT)


def rename_test_url(base_url):
    return '{}{}'.format(base_url, RENAME_TEST_ENDPOINT)


def save_test_url(base_url):
    return '{}{}'.format(base_url, SAVE_TEST_ENDPOINT)


def save_test_code_url(base_url):
    return '{}{}'.format(base_url, SAVE_TEST_CODE_ENDPOINT)


def delete_test(project_name, test_name, user=None):
    return requests.delete(delete_test_url(execution.data.env.url),
                           headers=utils.common_headers(user),
                           json={'project': project_name, 'fullPath': test_name})


def duplicate_test(project_name, test_name, new_test_name, user=None):
    json_ = {
        'project': project_name,
        'fullPath': test_name,
        'newFileFullPath': new_test_name
    }
    return requests.post(duplicate_test_url(execution.data.env.url),
                         headers=utils.common_headers(user), json=json_)


def rename_test(project_name, test_name, new_test_name, user=None):
    json_ = {
        'project': project_name,
        'fullFilename': test_name,
        'newFullFilename': new_test_name
    }
    return requests.post(rename_test_url(execution.data.env.url),
                         headers=utils.common_headers(user), json=json_)


def run_test(project_name, test_name, browsers=[], environments=[], processes=1, user=None):
    json_ = {
        'project': project_name,
        'testName': test_name,
        'browsers': browsers,
        'environments': environments,
        'processes': processes
    }
    return requests.post(run_test_url(execution.data.env.url),
                         headers=utils.common_headers(user), json=json_)


def save_test(project_name, test_name, description, pages, test_data, steps, tags, user=None):
    json_ = {
        'project': project_name,
        'testName': test_name,
        'description': description,
        'pages': pages,
        'testData': test_data,
        'steps': steps,
        'tags': tags,
    }
    return requests.put(save_test_url(execution.data.env.url),
                        headers=utils.common_headers(user), json=json_)


def save_test_code(project_name, test_name, test_data, content, user=None):
    json_ = {
        'project': project_name,
        'testName': test_name,
        'testData': test_data,
        'content': content,
    }
    return requests.put(save_test_code_url(execution.data.env.url),
                        headers=utils.common_headers(user), json=json_)
