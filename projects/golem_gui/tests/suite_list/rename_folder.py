from golem import actions

from projects.golem_gui.pages import common
from projects.golem_gui.pages import api
from projects.golem_gui.pages import suite_list


def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    api.project.create_access_random_project()
    common.navigate_menu('Suites')
    actions.store('folder', actions.random_str())
    suite_list.add_folder(data.folder)
    actions.refresh_page()


def test(data):
    suite_list.dismiss_no_tests_alert_if()
    new_folder = data.folder + '_rename'
    suite_list.rename_folder(data.folder, new_folder)
    assert not suite_list.folder_exists(data.folder)
    assert suite_list.folder_exists(new_folder)
    actions.refresh_page()
    assert not suite_list.folder_exists(data.folder)
    assert suite_list.folder_exists(new_folder)


def teardown(data):
    api.project.delete_project(data.project)
