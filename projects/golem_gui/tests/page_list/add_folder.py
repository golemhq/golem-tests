from golem import actions

from projects.golem_gui.pages import common
from projects.golem_gui.pages import page_list
from projects.golem_gui.pages import api


description = 'Verify the user can create a new folder from the page list page'


def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    api.project.create_access_random_project()
    common.navigate_menu('Pages')


def test(data):
    folder_one = actions.random_str()
    page_list.add_folder(folder_one)
    page_list.assert_folder_exists(folder_one)
    folder_two = 'folder1.' + actions.random_str()
    page_list.add_folder(folder_two)
    page_list.assert_folder_exists(folder_two)
    actions.refresh_page()
    page_list.assert_folder_exists(folder_one)
    page_list.assert_folder_exists(folder_two)


def teardown(data):
    api.project.delete_project(data.project)
