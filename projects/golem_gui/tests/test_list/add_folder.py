from golem import actions

from projects.golem_gui.pages import common
from projects.golem_gui.pages import api
from projects.golem_gui.pages import test_list


description = 'Verify the user can create a new folder from the test list page'

tags = ['smoke']


def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    api.project.using_project('test_list')
    common.navigate_menu('Tests')


def test(data):
    folder_one = actions.random_str()
    test_list.add_folder(folder_one)
    test_list.assert_folder_exists(folder_one)
    folder_two = 'folder1.' + actions.random_str()
    test_list.add_folder(folder_two)
    test_list.assert_folder_exists(folder_two)
    actions.refresh_page()
    test_list.assert_folder_exists(folder_one)
    test_list.assert_folder_exists(folder_two)
