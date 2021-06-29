from golem import actions

from projects.golem_api.pages.project import get_projects as api_get_projects
from projects.golem_api.pages.users import create_new_user as api_create_new_user
from projects.golem_gui.pages import common
from projects.golem_gui.pages import test_list
from projects.golem_gui.pages import suite_list
from projects.golem_gui.pages import suite_builder
from projects.golem_gui.pages import test_builder
from projects.golem_gui.pages import api


def create_success_test(project_name, test_name=None):
    if test_name is None:
        test_name = actions.random_str()
    code = 'def test_one(data):\n' \
           '    wait(2)\n' \
           '    pass'
    api.test.create_test_with_code(project_name, test_name, code)
    return test_name


def create_error_test(project_name, test_name=None):
    if test_name is None:
        test_name = actions.random_str()
    code = 'def test_one(data):\n' \
           '    wait(2)\n' \
           '    error("error message")'
    api.test.create_test_with_code(project_name, test_name, code)
    return test_name


def create_failing_test(project_name, test_name=None):
    if test_name is None:
        test_name = actions.random_str()
    code = 'def test_one(data):\n' \
           '    wait(2)\n' \
           '    fail("failure message")'
    api.test.create_test_with_code(project_name, test_name, code)
    return test_name


def create_access_simple_suite(suite_name=None, test_name=None):
    """Creates a suite with an empty test if the suite
    does not exist.
    """
    suite_name = suite_name or 'simple_suite'
    test_name = test_name or 'simple_test'
    common.navigate_menu('Tests')
    if not test_list.test_exists(test_name):
        test_list.add_test(test_name)
    common.navigate_menu('Suites')
    if not suite_list.suite_exists(suite_name):
        suite_list.add_suite(suite_name)
        suite_list.access_suite(suite_name)
        suite_builder.select_test(test_name)
        suite_builder.save_suite()
    else:
        suite_list.access_suite(suite_name)


# TODO move to an 'api' utils

def get_projects():
    return api_get_projects().json()


def create_user(username, password, email=None, is_superuser=False, project_permissions=None):
    api_create_new_user(username, password, email, is_superuser, project_permissions)


def create_random_user():
    username = actions.random_str()
    password = actions.random_str()
    create_user(username, password)
    return {'username': username, 'password': password}
