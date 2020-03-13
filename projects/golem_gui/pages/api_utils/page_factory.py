from golem import actions

from projects.golem_api.pages import project as project_api
from projects.golem_gui.pages import urls


def create_page(project_name, page_name):
    project_api.create_page(project_name, page_name)


def create_access_page(project_name, page_name):
    create_page(project_name, page_name)
    actions.get_browser().navigate(urls.page(project_name, page_name))


def create_access_random_page(project_name):
    page_name = actions.random_str()
    actions.get_data().page_name = page_name
    create_access_page(project_name, page_name)
