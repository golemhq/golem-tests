from golem import actions

from projects.golem_gui.pages import common
from projects.golem_gui.pages import page_list
from projects.golem_gui.pages import api


description = 'Verify the user can create a new folder from the page list page'


def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    api.project.using_project('page_list')
    common.navigate_menu('Pages')


def test_add_folder(data):
    folder_one = actions.random_str()
    page_list.add_folder(folder_one)
    assert page_list.folder_exists(folder_one)

    folder_two = 'folder1.' + actions.random_str()
    page_list.add_folder(folder_two)
    assert page_list.folder_exists(folder_two)

    actions.refresh_page()
    assert page_list.folder_exists(folder_one)
    assert page_list.folder_exists(folder_two)
