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


def test_add_folder_max_length(data):
    test_list.add_folder('a'*151)
    common.assert_error_message('Maximum name length is 150 characters')


def test_add_folder_invalid_chars(data):
    actions.refresh_page()
    test_list.add_folder('a-b-c')
    common.assert_error_message('Only letters, numbers and underscores are allowed')


def test_add_folder_with_spaces(data):
    actions.refresh_page()
    test_list.add_folder('a b')
    common.assert_error_message('Only letters, numbers and underscores are allowed')


def test_add_folder_existing_name(data):
    actions.refresh_page()
    test_list.add_folder('test')
    test_list.add_folder('test')
    common.assert_error_message('A directory with that name already exists')
