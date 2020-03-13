from golem import actions

from projects.golem_gui.pages import common
from projects.golem_gui.pages import api
from projects.golem_gui.pages import test_list


description = 'Verify the user can create a new test from the test list page'

tags = ['smoke']


def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    api.project.create_access_random_project()
    common.navigate_menu('Tests')


def test(data):
    # to root
    test_one = actions.random_str()
    test_list.add_test(test_one)
    test_list.assert_test_exists(test_one)
    # to folder
    test_two = 'folder1.' + actions.random('ddddd')
    test_list.add_test(test_two)
    test_list.assert_test_exists(test_two)
    actions.refresh_page()
    test_list.assert_test_exists(test_one)
    test_list.assert_test_exists(test_two)


def teardown(data):
    api.project.delete_project(data.project)
