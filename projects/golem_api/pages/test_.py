import requests

from projects.golem_api.pages.utils import url, headers


TEST_COMPONENTS_ENDPOINT = '/test/components'
DELETE_TEST_ENDPOINT = '/test/delete'
DUPLICATE_TEST_ENDPOINT = '/test/duplicate'
RENAME_TEST_ENDPOINT = '/test/rename'
RUN_TEST_ENDPOINT = '/test/run'
SAVE_TEST_ENDPOINT = '/test/save'
SAVE_TEST_CODE_ENDPOINT = '/test/code/save'
RENAME_TEST_DIRECTORY_ENDPOINT = '/test/directory/rename'
DELETE_TEST_DIRECTORY_ENDPOINT = '/test/directory/delete'


def get_test_components(project_name, test_name, user=None):
    return requests.get(url(TEST_COMPONENTS_ENDPOINT), headers=headers(user),
                        params={'project': project_name, 'test': test_name})


def delete_test(project_name, test_name, user=None):
    return requests.delete(url(DELETE_TEST_ENDPOINT), headers=headers(user),
                           json={'project': project_name, 'fullPath': test_name})


def duplicate_test(project_name, test_name, new_test_name, user=None):
    json_ = {
        'project': project_name,
        'fullPath': test_name,
        'newFileFullPath': new_test_name
    }
    return requests.post(url(DUPLICATE_TEST_ENDPOINT), headers=headers(user), json=json_)


def rename_test(project_name, test_name, new_test_name, user=None):
    json_ = {
        'project': project_name,
        'fullFilename': test_name,
        'newFullFilename': new_test_name
    }
    return requests.post(url(RENAME_TEST_ENDPOINT), headers=headers(user), json=json_)


def run_test(project_name, test_name, test_functions=[], browsers=[], environments=[], processes=1, user=None):
    json_ = {
        'project': project_name,
        'testName': test_name,
        'testFunctions': test_functions,
        'browsers': browsers,
        'environments': environments,
        'processes': processes
    }
    return requests.post(url(RUN_TEST_ENDPOINT), headers=headers(user), json=json_)


def save_test(project_name, test_name, description='', pages=None, test_data=None, steps=None, tags=None,
              skip=False, user=None):
    if pages is None:
        pages = []
    if test_data is None:
        test_data = []
    if steps is None:
        steps = {
            'setup': [],
            'tests': {
                'test_name': []
            },
            'teardown': []
        }
    if tags is None:
        tags = []

    json_ = {
        'project': project_name,
        'testName': test_name,
        'description': description,
        'pages': pages,
        'testData': test_data,
        'steps': steps,
        'tags': tags,
        'skip': skip
    }
    return requests.put(url(SAVE_TEST_ENDPOINT), headers=headers(user), json=json_)


def save_test_code(project_name, test_name, test_data, content, user=None):
    json_ = {
        'project': project_name,
        'testName': test_name,
        'testData': test_data,
        'content': content,
    }
    return requests.put(url(SAVE_TEST_CODE_ENDPOINT), headers=headers(user), json=json_)


def rename_test_directory(project_name, dir_name, new_dir_name, user=None):
    json_ = {
        'project': project_name,
        'fullDirname': dir_name,
        'newFullDirname': new_dir_name
    }
    return requests.post(url(RENAME_TEST_DIRECTORY_ENDPOINT), headers=headers(user), json=json_)


def delete_test_directory(project_name, dir_name, user=None):
    return requests.delete(url(DELETE_TEST_DIRECTORY_ENDPOINT), headers=headers(user),
                           json={'project': project_name, 'fullDirname': dir_name})
