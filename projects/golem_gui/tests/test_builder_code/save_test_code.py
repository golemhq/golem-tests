from golem import actions

from projects.golem_gui.pages import common
from projects.golem_gui.pages import api
from projects.golem_gui.pages import index
from projects.golem_gui.pages import test_builder
from projects.golem_gui.pages import test_builder_code


description = 'Verify the user can edit test code and save it'

tags = ['smoke']


def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    index.create_access_project('test')
    actions.store('test_name', actions.random_str())
    api.test.create_access_test('test', data.test_name)
    actions.click(test_builder.code_button)


def test(data):
    test_line = "description = 'desc'"
    test_builder_code.set_value(test_line)
    actions.click(test_builder_code.save_button)
    common.assert_toast_message_is_displayed('Test '+data.test_name+' saved')
    actions.refresh_page()
    test_builder_code.assert_value(test_line)
