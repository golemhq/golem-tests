from golem import actions

from projects.golem_gui.pages import common
from projects.golem_gui.pages import api
from projects.golem_gui.pages import suite_list


description = 'Verify the user can create a new folder from the suite list page'


def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    api.project.using_project('suite_list')
    common.navigate_menu('Suites')


def test(data):
    folder_one = actions.random_str()
    suite_list.add_folder(folder_one)
    suite_list.assert_folder_exists(folder_one)

    folder_two = '{}.{}'.format(actions.random_str(), actions.random_str())
    suite_list.add_folder(folder_two)
    suite_list.assert_folder_exists(folder_two)

    actions.refresh_page()
    suite_list.assert_folder_exists(folder_one)
    suite_list.assert_folder_exists(folder_two)
