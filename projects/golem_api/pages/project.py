import json

import requests

from golem import execution

from projects.golem_api.pages import utils


PROJECT_EXISTS_ENDPOINT = 'api/project-exists'
CREATE_PROJECT_ENDPOINT = 'api/project'
CREATE_PROJECT_TEST_ENDPOINT = 'api/project/test'
CREATE_PROJECT_PAGE_ENDPOINT = 'api/project/page'
CREATE_PROJECT_SUITE_ENDPOINT = 'api/project/suite'
PROJECT_TEST_TREE_ENDPOINT = 'api/project/test-tree'
PROJECT_PAGE_TREE_ENDPOINT = 'api/project/page-tree'
PROJECT_SUITE_TREE_ENDPOINT = 'api/project/suite-tree'
GET_PAGES_ENDPOINT = 'api/project/pages'
GET_PROJECT_SUPPORTED_BROWSERS_ENDPOINT = 'api/project/supported-browsers'
PROJECT_ENVIRONMENTS_ENDPOINT = 'api/project/environments'
PROJECT_PAGE_EXISTS_ENDPOINT = 'api/project/page-exists'
PROJECT_HAS_TESTS_ENDPOINT = 'api/project/has-tests'
PROJECT_TEST_TAGS_ENDPOINT = 'api/project/test-tags'
PROJECT_TAGS_ENDPOINT = 'api/project/tags'
PROJECT_HEALTH_ENDPOINT = 'api/project/health'
PROJECT_SAVE_ENVIRONMENTS_ENDPOINT = 'api/project/environments/save'


# URLs

def project_exists_url(base_url):
    return '{}{}'.format(base_url, PROJECT_EXISTS_ENDPOINT)


def project_test_tree_url(base_url):
    return '{}{}'.format(base_url, PROJECT_TEST_TREE_ENDPOINT)


def project_page_tree_url(base_url):
    return '{}{}'.format(base_url, PROJECT_PAGE_TREE_ENDPOINT)


def project_suite_tree_url(base_url):
    return '{}{}'.format(base_url, PROJECT_SUITE_TREE_ENDPOINT)


def create_project_url(base_url):
    return '{}{}'.format(base_url, CREATE_PROJECT_ENDPOINT)


def create_project_test_url(base_url):
    return '{}{}'.format(base_url, CREATE_PROJECT_TEST_ENDPOINT)


def create_project_page_url(base_url):
    return '{}{}'.format(base_url, CREATE_PROJECT_PAGE_ENDPOINT)


def create_project_suite_url(base_url):
    return '{}{}'.format(base_url, CREATE_PROJECT_SUITE_ENDPOINT)


def get_project_pages_url(base_url):
    return '{}{}'.format(base_url, GET_PAGES_ENDPOINT)


def get_project_supported_browsers_url(base_url):
    return '{}{}'.format(base_url, GET_PROJECT_SUPPORTED_BROWSERS_ENDPOINT)


def project_environments_url(base_url):
    return '{}{}'.format(base_url, PROJECT_ENVIRONMENTS_ENDPOINT)


def project_page_exists_url(base_url):
    return '{}{}'.format(base_url, PROJECT_PAGE_EXISTS_ENDPOINT)


def project_has_tests_url(base_url):
    return '{}{}'.format(base_url, PROJECT_HAS_TESTS_ENDPOINT)


def project_test_tags_url(base_url):
    return '{}{}'.format(base_url, PROJECT_TEST_TAGS_ENDPOINT)


def project_tags_url(base_url):
    return '{}{}'.format(base_url, PROJECT_TAGS_ENDPOINT)


def project_health_url(base_url):
    return '{}{}'.format(base_url, PROJECT_HEALTH_ENDPOINT)


def project_environments_save_url(base_url):
    return '{}{}'.format(base_url, PROJECT_SAVE_ENVIRONMENTS_ENDPOINT)


# REQUESTS

def get_project_exists(project_name, user=None):
    return requests.get(project_exists_url(execution.data.env.url),
                        headers=utils.common_headers(user),
                        json={'project': project_name})


def create_project(project_name, user=None):
    return requests.post(create_project_url(execution.data.env.url),
                         headers=utils.common_headers(user),
                         json={'project': project_name})


def create_project_if(project_name, user=None):
    """Create a project only if it does not already exist"""
    if not get_project_exists(project_name, user).json():
        response = create_project(project_name, user)
        if response.status_code != 200 or response.json()['errors'] != []:
            raise Exception('Error creating project {}'.format(project_name))


def create_project_test(project_name, test_name, is_dir=False, user=None):
    json_ = {
        'project': project_name,
        'isDir': is_dir,
        'fullPath': test_name
    }
    return requests.post(create_project_test_url(execution.data.env.url),
                         headers=utils.common_headers(user), json=json_)


def create_project_page(project_name, page_name, is_dir=False, user=None):
    json_ = {
        'project': project_name,
        'isDir': is_dir,
        'fullPath': page_name
    }
    return requests.post(create_project_page_url(execution.data.env.url),
                         headers=utils.common_headers(user), json=json_)


def create_project_suite(project_name, suite_name, is_dir=False, user=None):
    json_ = {
        'project': project_name,
        'isDir': is_dir,
        'fullPath': suite_name
    }
    return requests.post(create_project_suite_url(execution.data.env.url),
                         headers=utils.common_headers(user), json=json_)


def get_project_test_tree(project_name, user=None):
    return requests.get(project_test_tree_url(execution.data.env.url),
                        headers=utils.common_headers(user),
                        params={'project': project_name})


def get_project_page_tree(project_name, user=None):
    return requests.get(project_page_tree_url(execution.data.env.url),
                        headers=utils.common_headers(user),
                        params={'project': project_name})


def get_project_suite_tree(project_name, user=None):
    return requests.get(project_suite_tree_url(execution.data.env.url),
                        headers=utils.common_headers(user),
                        params={'project': project_name})


def get_pages(project_name, user=None):
    return requests.get(get_project_pages_url(execution.data.env.url),
                        headers=utils.common_headers(user),
                        params={'project': project_name})


def get_supported_browsers(project_name, user=None):
    return requests.get(get_project_supported_browsers_url(execution.data.env.url),
                        headers=utils.common_headers(user),
                        params={'project': project_name})


def get_project_environments(project_name, user=None):
    return requests.get(project_environments_url(execution.data.env.url),
                        headers=utils.common_headers(user),
                        params={'project': project_name})


def get_project_page_exists(project_name, page_name, user=None):
    return requests.get(project_page_exists_url(execution.data.env.url),
                        headers=utils.common_headers(user),
                        params={'project': project_name, 'page': page_name})


def get_project_has_tests(project_name, user=None):
    return requests.get(project_has_tests_url(execution.data.env.url),
                        headers=utils.common_headers(user),
                        params={'project': project_name})


def get_project_test_tags(project_name, user=None):
    return requests.get(project_test_tags_url(execution.data.env.url),
                        headers=utils.common_headers(user),
                        params={'project': project_name})


def get_project_tags(project_name, user=None):
    return requests.get(project_tags_url(execution.data.env.url),
                        headers=utils.common_headers(user),
                        params={'project': project_name})


def get_project_health(project_name, user=None):
    return requests.get(project_health_url(execution.data.env.url),
                        headers=utils.common_headers(user),
                        params={'project': project_name})


def save_environments(project_name, env_data, user=None):
    env_data = json.dumps(env_data)
    return requests.put(project_environments_save_url(execution.data.env.url),
                        headers=utils.common_headers(user),
                        json={'project': project_name, 'environmentData': env_data})
