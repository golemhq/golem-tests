from golem import actions

from projects.golem_gui.pages import common
from projects.golem_gui.pages import api
from projects.golem_gui.pages import test_builder_code


description = 'Verify the application displays an error message when the user saves test code with errors'


def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    api.project.using_project('test_builder_code')
    data.test = api.test.create_access_test_code(data.project)


def test(data):
    page_line = "undefined_var"
    error_message = "Traceback (most recent call last):\nNameError: name 'undefined_var' is not defined"
    test_builder_code.set_value(page_line)
    actions.click(test_builder_code.save_button)
    common.assert_toast_message_is_displayed('Test '+data.test+' saved')
    common.assert_toast_message_is_displayed('There are errors in the code')
    test_builder_code.assert_error_message(error_message)
    actions.refresh_page()
    test_builder_code.assert_error_message(error_message)
