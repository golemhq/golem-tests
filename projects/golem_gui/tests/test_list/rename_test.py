from golem import actions

from projects.golem_gui.pages import common
from projects.golem_gui.pages import api
from projects.golem_gui.pages import test_list


description = 'Verify the user can rename a test from the test list'


def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    api.project.using_project('test_list')
    data.test = api.test.create_test(data.project)
    common.navigate_menu('Tests')


def test(data):
    new_name = data.test + '_rename'
    test_list.rename_test(data.test, new_name)
    assert not test_list.test_exists(data.test)
    test_list.assert_test_exists(new_name)
    actions.refresh_page()
    test_list.assert_test_exists(new_name)
