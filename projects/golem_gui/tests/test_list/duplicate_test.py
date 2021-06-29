from golem import actions

from projects.golem_gui.pages import common
from projects.golem_gui.pages import api
from projects.golem_gui.pages import test_list


description = 'Verify the user can duplicate a test and tags are displayed for duplicated test'


def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    api.project.using_project('test_list')
    data.test = api.test.create_test(data.project)
    common.navigate_menu('Tests')


def test(data):
    new_name = data.test + 'copy'
    test_list.duplicate_test(data.test, new_name)
    # to folder
    new_name_two = 'test.{}'.format(new_name)
    test_list.duplicate_test(new_name, new_name_two)
    test_list.assert_test_exists(data.test)
    test_list.assert_test_exists(new_name)
    test_list.assert_test_exists(new_name_two)
    actions.refresh_page()
    test_list.assert_test_exists(data.test)
    test_list.assert_test_exists(new_name)
    test_list.assert_test_exists(new_name_two)
