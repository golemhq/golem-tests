from golem import actions

from projects.golem_api.pages import project as project_api
from projects.golem_api.pages import test_ as test_api
from projects.golem_gui.pages import urls


def create_test(project_name, test_name=None):
    if test_name is None:
        test_name = actions.random_str()
    project_api.create_test(project_name, test_name)
    return test_name


def create_access_test(project_name, test_name=None):
    test_name = create_test(project_name, test_name)
    actions.get_browser().navigate(urls.test(project_name, test_name))
    return test_name


def create_access_test_code(project_name, test_name=None):
    test_name = create_test(project_name, test_name)
    actions.get_browser().navigate(urls.test_code(project_name, test_name))
    return test_name


def create_test_with_code(project_name, test_name, code):
    create_test(project_name, test_name)
    test_api.save_test_code(project_name, test_name, [], code)
    return test_name
