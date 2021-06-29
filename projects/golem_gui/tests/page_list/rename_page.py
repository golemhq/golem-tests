from golem import actions

from projects.golem_gui.pages import common
from projects.golem_gui.pages import page_list
from projects.golem_gui.pages import api


def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    api.project.using_project('page_list')
    data.page = api.page.create_page(data.project)
    common.navigate_menu('Pages')


def test_rename_page(data):
    new_name = data.page + '_rename'
    page_list.rename_page(data.page, new_name)
    assert not page_list.page_exists(data.page)
    assert page_list.page_exists(new_name)
    actions.refresh_page()
    assert page_list.page_exists(new_name)
