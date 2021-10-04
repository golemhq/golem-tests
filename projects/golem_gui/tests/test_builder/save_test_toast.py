from golem import actions

from projects.golem_gui.pages import common
from projects.golem_gui.pages import api
from projects.golem_gui.pages import test_builder


description = 'Verify the application displays a toast message when saving a test'

tags = ['smoke']


def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    api.project.using_project('test_builder')
    data.test = api.test.create_access_test(data.project)


def test_toast_is_displayed_when_saving_changes(data):
    test_builder.add_step_to_test('test', 'click')
    actions.click(test_builder.save_button)
    common.assert_toast_message_is_displayed('Test '+data.test+' saved')


def test_toast_is_displayed_with_no_changes(data):
    actions.refresh_page()
    actions.click(test_builder.save_button)
    common.assert_toast_message_is_displayed('Test '+data.test+' saved')
