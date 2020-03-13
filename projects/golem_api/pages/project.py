import json

import requests

from golem import actions

from projects.golem_api.pages.utils import url, headers


PROJECT_EXISTS_ENDPOINT = '/project-exists'
CREATE_PROJECT_ENDPOINT = '/project'
CREATE_TEST_ENDPOINT = '/project/test'
CREATE_PAGE_ENDPOINT = '/project/page'
CREATE_SUITE_ENDPOINT = '/project/suite'
CREATE_TEST_DIRECTORY_ENDPOINT = '/project/test/directory'
CREATE_PAGE_DIRECTORY_ENDPOINT = '/project/page/directory'
CREATE_SUITE_DIRECTORY_ENDPOINT = '/project/suite/directory'
DELETE_PROJECT_ENDPOINT = '/project/delete'
TEST_TREE_ENDPOINT = '/project/test-tree'
PAGE_TREE_ENDPOINT = '/project/page-tree'
SUITE_TREE_ENDPOINT = '/project/suite-tree'
GET_PAGES_ENDPOINT = '/project/pages'
GET_PROJECT_SUPPORTED_BROWSERS_ENDPOINT = '/project/supported-browsers'
PROJECT_ENVIRONMENTS_ENDPOINT = '/project/environments'
PAGE_EXISTS_ENDPOINT = '/project/page-exists'
TEST_EXISTS_ENDPOINT = '/project/test-exists'
SUITE_EXISTS_ENDPOINT = '/project/suite-exists'
PROJECT_HAS_TESTS_ENDPOINT = '/project/has-tests'
TEST_TAGS_ENDPOINT = '/project/test-tags'
PROJECT_TAGS_ENDPOINT = '/project/tags'
PROJECT_HEALTH_ENDPOINT = '/project/health'
SAVE_ENVIRONMENTS_ENDPOINT = '/project/environments/save'
GET_PROJECTS_ENDPOINT = '/projects'


def get_project_exists(project_name, user=None):
    return requests.get(url(PROJECT_EXISTS_ENDPOINT), headers=headers(user),
                        json={'project': project_name})


def create_project(project_name, user=None):
    return requests.post(url(CREATE_PROJECT_ENDPOINT), headers=headers(user),
                         json={'project': project_name})


def create_test(project_name, test_name, user=None):
    json_ = {
        'project': project_name,
        'fullPath': test_name
    }
    return requests.post(url(CREATE_TEST_ENDPOINT), headers=headers(user), json=json_)


def create_page(project_name, page_name, user=None):
    json_ = {
        'project': project_name,
        'fullPath': page_name
    }
    return requests.post(url(CREATE_PAGE_ENDPOINT), headers=headers(user), json=json_)


def create_suite(project_name, suite_name, user=None):
    json_ = {
        'project': project_name,
        'fullPath': suite_name
    }
    return requests.post(url(CREATE_SUITE_ENDPOINT), headers=headers(user), json=json_)


def create_test_directory(project_name, dir_name, user=None):
    json_ = {
        'project': project_name,
        'fullPath': dir_name
    }
    return requests.post(url(CREATE_TEST_DIRECTORY_ENDPOINT), headers=headers(user), json=json_)


def create_page_directory(project_name, dir_name, user=None):
    json_ = {
        'project': project_name,
        'fullPath': dir_name
    }
    return requests.post(url(CREATE_PAGE_DIRECTORY_ENDPOINT), headers=headers(user), json=json_)


def create_suite_directory(project_name, dir_name, user=None):
    json_ = {
        'project': project_name,
        'fullPath': dir_name
    }
    return requests.post(url(CREATE_SUITE_DIRECTORY_ENDPOINT), headers=headers(user), json=json_)


def delete_project(project_name, user=None):
    return requests.delete(url(DELETE_PROJECT_ENDPOINT), headers=headers(user),
                           json={'project': project_name})


def get_test_tree(project_name, user=None):
    return requests.get(url(TEST_TREE_ENDPOINT), headers=headers(user),
                        params={'project': project_name})


def get_page_tree(project_name, user=None):
    return requests.get(url(PAGE_TREE_ENDPOINT), headers=headers(user),
                        params={'project': project_name})


def get_suite_tree(project_name, user=None):
    return requests.get(url(SUITE_TREE_ENDPOINT), headers=headers(user),
                        params={'project': project_name})


def get_pages(project_name, user=None):
    return requests.get(url(GET_PAGES_ENDPOINT), headers=headers(user),
                        params={'project': project_name})


def get_supported_browsers(project_name, user=None):
    return requests.get(url(GET_PROJECT_SUPPORTED_BROWSERS_ENDPOINT),
                        headers=headers(user), params={'project': project_name})


def get_project_environments(project_name, user=None):
    return requests.get(url(PROJECT_ENVIRONMENTS_ENDPOINT), headers=headers(user),
                        params={'project': project_name})


def get_page_exists(project_name, page_name, user=None):
    return requests.get(url(PAGE_EXISTS_ENDPOINT), headers=headers(user),
                        params={'project': project_name, 'page': page_name})


def get_test_exists(project_name, test_name, user=None):
    return requests.get(url(TEST_EXISTS_ENDPOINT), headers=headers(user),
                        params={'project': project_name, 'test': test_name})


def get_suite_exists(project_name, suite_name, user=None):
    return requests.get(url(SUITE_EXISTS_ENDPOINT), headers=headers(user),
                        params={'project': project_name, 'suite': suite_name})


def get_project_has_tests(project_name, user=None):
    return requests.get(url(PROJECT_HAS_TESTS_ENDPOINT), headers=headers(user),
                        params={'project': project_name})


def get_project_test_tags(project_name, user=None):
    return requests.get(url(TEST_TAGS_ENDPOINT), headers=headers(user),
                        params={'project': project_name})


def get_project_tags(project_name, user=None):
    return requests.get(url(PROJECT_TAGS_ENDPOINT), headers=headers(user),
                        params={'project': project_name})


def get_project_health(project_name, user=None):
    return requests.get(url(PROJECT_HEALTH_ENDPOINT), headers=headers(user),
                        params={'project': project_name})


def save_environments(project_name, env_data, user=None):
    env_data = json.dumps(env_data)
    return requests.put(url(SAVE_ENVIRONMENTS_ENDPOINT), headers=headers(user),
                        json={'project': project_name, 'environmentData': env_data})


def get_projects(user=None):
    return requests.get(url(GET_PROJECTS_ENDPOINT), headers=headers(user))


# UTILS


def create_project_if(project_name, user=None):
    """Create a project only if it does not already exist"""
    if not get_project_exists(project_name, user).json():
        response = create_project(project_name, user)
        if response.status_code != 200 or response.json()['errors'] != []:
            raise Exception('Error creating project {}'.format(project_name))


def using_project(project_name, user=None):
    """Create project if it does not exist, store it in data.project"""
    create_project_if(project_name, user)
    actions.store('project', project_name)


def create_random_project():
    project_name = actions.random_str()
    actions.step('Create project: {}'.format(project_name))
    create_project(project_name)
    return project_name


def create_random_page(project_name):
    page_name = actions.random_str()
    actions.step('Create page: {}'.format(page_name))
    create_page(project_name, page_name)
    return page_name


def create_random_suite(project_name):
    suite_name = actions.random_str()
    actions.step('Create suite: {}'.format(suite_name))
    create_suite(project_name, suite_name)
    return suite_name


def create_random_test(project_name):
    test_name = actions.random_str()
    actions.step('Create test: {}'.format(test_name))
    create_test(project_name, test_name)
    return test_name

