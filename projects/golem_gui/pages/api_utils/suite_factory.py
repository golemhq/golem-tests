from golem import actions

from projects.golem_api.pages import project as project_api
from projects.golem_api.pages import suite as suite_api
from projects.golem_gui.pages import urls


def create_suite(project_name, suite_name=None, tests=None):
    if suite_name is None:
        suite_name = actions.random_str()
    project_api.create_suite(project_name, suite_name)
    if tests is not None:
        suite_api.save_suite(project_name, suite_name, tests)
    return suite_name


def create_access_suite(project_name, suite_name=None, tests=None):
    suite_name = create_suite(project_name, suite_name, tests)
    actions.get_browser().navigate(urls.suite(project_name, suite_name))
    return suite_name
