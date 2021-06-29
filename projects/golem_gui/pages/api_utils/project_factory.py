from golem import actions, browser

from projects.golem_api.pages import project as project_api
from projects.golem_gui.pages import urls


def create_project_if(project_name):
    if not project_api.project_exists(project_name):
        project_api.create_project(project_name)


def create_access_project(project_name):
    if not project_api.project_exists(project_name):
        project_api.create_project(project_name)
    browser.get_browser().navigate(urls.project(project_name))


def create_access_random_project():
    project_name = actions.random_str()
    actions.get_data().project = project_name
    project_api.create_project(project_name)
    browser.get_browser().navigate(urls.project(project_name))


def using_project(project_name):
    create_project_if(project_name)
    actions.get_data().project = project_name
    browser.get_browser().navigate(urls.project(project_name))


def delete_project(project_name):
    project_api.delete_project(project_name)


def set_environments(project_name, env_value):
    project_api.save_environments(project_name, env_value)
