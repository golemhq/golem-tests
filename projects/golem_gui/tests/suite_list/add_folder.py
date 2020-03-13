from golem import actions

from projects.golem_gui.pages import common
from projects.golem_gui.pages import api
from projects.golem_gui.pages import suite_list


description = 'Verify the user can create a new folder from the suite list page'


def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    api.project.create_access_random_project()
    common.navigate_menu('Suites')


def test(data):
    actions.store('folder_one', actions.random_str())
    suite_list.add_folder(data.folder_one)
    suite_list.assert_folder_exists(data.folder_one)
    actions.store('folder_two', 'folder1.' + actions.random_str())
    suite_list.add_folder(data.folder_two)
    suite_list.assert_folder_exists(data.folder_two)
    actions.refresh_page()
    suite_list.assert_folder_exists(data.folder_one)
    suite_list.assert_folder_exists(data.folder_two)


def teardown(data):
    api.project.delete_project(data.project)
