from golem import actions

from projects.golem_api.pages import project as project_api
from projects.golem_gui.pages import urls


def create_suite(project_name, suite_name):
    project_api.create_suite(project_name, suite_name)


def create_access_suite(project_name, suite_name):
    project_api.create_suite(project_name, suite_name)
    actions.get_browser().navigate(urls.suite(project_name, suite_name))


def create_access_random_suite(project_name):
    suite_name = actions.random_str()
    actions.get_data().suite_name = suite_name
    create_access_suite(project_name, suite_name)
