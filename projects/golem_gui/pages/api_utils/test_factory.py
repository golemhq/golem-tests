from golem import actions

from projects.golem_api.pages import project as project_api
from projects.golem_gui.pages import urls


def create_test(project_name, test_name):
    project_api.create_test(project_name, test_name)


def create_access_test(project_name, test_name):
    project_api.create_test(project_name, test_name)
    actions.get_browser().navigate(urls.test(project_name, test_name))


def create_access_random_test(project_name):
    test_name = actions.random_str()
    actions.get_data().test_name = test_name
    create_access_test(project_name, test_name)
