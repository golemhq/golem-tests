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
    test_list.delete_test(data.test)
    common.assert_toast_message_is_displayed('File {} was removed'.format(data.test))
    assert not test_list.test_exists(data.test)
    actions.refresh_page()
    assert not test_list.test_exists(data.test)
