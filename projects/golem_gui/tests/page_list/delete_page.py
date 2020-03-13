from golem import actions

from projects.golem_gui.pages import common
from projects.golem_gui.pages import page_list
from projects.golem_gui.pages import api


description = 'Verify the user can rename a page from the page list'


def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    api.project.create_access_random_project()
    actions.store('page', actions.random_str())
    api.page.create_page(data.project, data.page)
    common.navigate_menu('Pages')


def test(data):
    page_list.delete_page(data.page)
    assert not page_list.page_exists(data.page)
    actions.refresh_page()
    assert not page_list.page_exists(data.page)


def teardown(data):
    api.project.delete_project(data.project)
