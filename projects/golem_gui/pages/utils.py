from golem import actions

from projects.golem_api.pages.project import get_projects as api_get_projects
from projects.golem_api.pages.users import create_new_user as api_create_new_user
from projects.golem_gui.pages import common, test_list, suite_list, suite_builder, test_builder


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


def create_access_suite_with_different_results(suite_name):
    common.navigate_menu('Tests')
    if not test_list.test_exists('success_test'):
        test_list.create_access_test('success_test')
        test_builder.add_action('wait', ['3'])
        test_builder.add_action('step', ["\'success\'"])
        test_builder.save_test()
    common.navigate_menu('Tests')
    if not test_list.test_exists('failing_test'):
        test_list.create_access_test('failing_test')
        test_builder.add_action('wait', ['3'])
        test_builder.add_action('fail', ["\'failure message\'"])
        test_builder.save_test()
    common.navigate_menu('Tests')
    if not test_list.test_exists('error_test'):
        test_list.create_access_test('error_test')
        test_builder.add_action('wait', ['3'])
        test_builder.add_action('error', ["\'error message\'"])
        test_builder.save_test()
    common.navigate_menu('Suites')
    if not suite_list.suite_exists(suite_name):
        suite_list.add_suite(suite_name)
        suite_list.access_suite(suite_name)
        suite_builder.select_test('success_test')
        suite_builder.select_test('failing_test')
        suite_builder.select_test('error_test')
        suite_builder.save_suite()
    else:
        suite_list.access_suite(suite_name)


# TODO move to an 'api' utils

def get_projects():
    return api_get_projects().json()


def create_user(username, password, email=None, is_superuser=False, project_permissions=None):
    api_create_new_user(username, password, email, is_superuser, project_permissions)


def create_random_user():
    username = actions.random('ddddd')
    password = actions.random('ddddd')
    create_user(username, password)
    return {'username': username, 'password': password}
