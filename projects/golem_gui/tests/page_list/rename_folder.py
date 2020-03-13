from golem import actions

from projects.golem_gui.pages import common
from projects.golem_gui.pages import page_list
from projects.golem_gui.pages import api


def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    api.project.create_access_random_project()
    common.navigate_menu('Pages')
    actions.store('folder', actions.random_str())
    page_list.add_folder(data.folder)
    actions.refresh_page()


def test(data):
    new_folder = data.folder + '_rename'
    page_list.rename_folder(data.folder, new_folder)
    assert not page_list.folder_exists(data.folder)
    assert page_list.folder_exists(new_folder)
    actions.refresh_page()
    assert not page_list.folder_exists(data.folder)
    assert page_list.folder_exists(new_folder)


def teardown(data):
    api.project.delete_project(data.project)
