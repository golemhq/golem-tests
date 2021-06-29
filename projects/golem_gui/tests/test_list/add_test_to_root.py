from golem import actions

from projects.golem_gui.pages import common
from projects.golem_gui.pages import api
from projects.golem_gui.pages import test_list


description = 'Verify the user can create a new test from the test list page'

tags = ['smoke']


def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    api.project.using_project('test_list')
    common.navigate_menu('Tests')


def test(data):
    test_one = '{}.{}'.format(actions.random_str(), actions.random_str())
    test_two = '{}.{}.{}'.format(actions.random_str(), actions.random_str(), actions.random_str())
    test_list.add_test_to_current_folder(test_one)
    test_list.add_test_to_current_folder(test_two)
    test_list.assert_test_exists(test_one)
    test_list.assert_test_exists(test_two)
    actions.refresh_page()
    test_list.assert_test_exists(test_one)
    test_list.assert_test_exists(test_two)
