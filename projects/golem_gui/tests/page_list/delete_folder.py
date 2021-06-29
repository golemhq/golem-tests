from golem import actions

from projects.golem_gui.pages import common
from projects.golem_gui.pages import page_list
from projects.golem_gui.pages import api


def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    api.project.using_project('page_list')
    common.navigate_menu('Pages')
    data.folder = actions.random_str()
    page_list.add_folder(data.folder)


def test_delete_folder(data):
    page_list.delete_folder(data.folder)
    assert not page_list.folder_exists(data.folder)
    actions.refresh_page()
    assert not page_list.folder_exists(data.folder)
