from golem import actions

from projects.golem_gui.pages import common
from projects.golem_gui.pages import api
from projects.golem_gui.pages import test_builder_code


description = 'Verify the user can edit test code and save it'

tags = ['smoke']


def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    api.project.using_project('test_builder_code')
    data.test = api.test.create_access_test_code(data.project)


def test(data):
    test_line = "description = 'desc'"
    test_builder_code.set_value(test_line)
    actions.click(test_builder_code.save_button)
    common.assert_toast_message_is_displayed('Test '+data.test+' saved')
    actions.refresh_page()
    test_builder_code.assert_value(test_line)
