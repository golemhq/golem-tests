from golem import actions

from projects.golem_gui.pages import common
from projects.golem_gui.pages import api
from projects.golem_gui.pages import test_list


def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    api.project.using_project('test_list')
    common.navigate_menu('Tests')


def test(data):
    test_name = 'invalid-name'
    test_list.add_test(test_name)
    common.assert_error_message('Only letters, numbers and underscores are allowed')
    assert not test_list.test_exists(test_name)
    actions.refresh_page()
    test_name = 'a'*151
    test_list.add_test(test_name)
    common.assert_error_message('Maximum name length is 150 characters')
    assert not test_list.test_exists(test_name)
