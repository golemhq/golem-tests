from golem import actions

from projects.golem_api.pages import project as project_api
from projects.golem_gui.pages import urls


def create_page(project_name, page_name=None):
    if page_name is None:
        page_name = actions.random_str()
    project_api.create_page(project_name, page_name)
    return page_name


def create_access_page(project_name, page_name=None):
    page_name = create_page(project_name, page_name)
    actions.get_browser().navigate(urls.page(project_name, page_name))
    return page_name


def create_dir(project_name, dirname):
    project_api.create_page_directory(project_name, dirname)


def create_random_dir(project_name):
    dirname = actions.random_str()
    create_dir(project_name, dirname)
    return dirname
