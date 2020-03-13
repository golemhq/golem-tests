from golem import actions

from projects.golem_gui.pages import common
from projects.golem_gui.pages import api
from projects.golem_gui.pages import test_list


description = 'Verify the user can create a new folder from the test list page'

tags = ['smoke']


def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    api.project.create_access_random_project()
    common.navigate_menu('Tests')


def test(data):
    # max length
    test_list.add_folder('a'*151)
    common.assert_error_message('Maximum name length is 150 characters')
    actions.refresh_page()
    # invalid chars
    test_list.add_folder('a-b-c')
    common.assert_error_message('Only letters, numbers and underscores are allowed')
    actions.refresh_page()
    # middle spaces
    test_list.add_folder('a b')
    common.assert_error_message('Only letters, numbers and underscores are allowed')
    actions.refresh_page()
    # existing folder
    test_list.add_folder('test')
    test_list.add_folder('test')
    common.assert_error_message('A directory with that name already exists')


def teardown(data):
    api.project.delete_project(data.project)
