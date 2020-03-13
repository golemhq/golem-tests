from golem import actions

from projects.golem_gui.pages import common
from projects.golem_gui.pages import page_list
from projects.golem_gui.pages import api


def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    api.project.create_access_random_project()
    actions.store('page', actions.random_str())
    api.page.create_page(data.project, data.page)
    common.navigate_menu('Pages')


def test(data):
    new_name = data.page + '_rename'
    page_list.rename_page(data.page, new_name)
    assert not page_list.page_exists(data.page)
    page_list.assert_page_exists(new_name)
    actions.refresh_page()
    page_list.assert_page_exists(new_name)


def teardown(data):
    api.project.delete_project(data.project)
