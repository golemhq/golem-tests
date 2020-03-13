from golem import actions

from projects.golem_gui.pages import common
from projects.golem_gui.pages import index
from projects.golem_gui.pages import api
from projects.golem_gui.pages import page_builder
from projects.golem_gui.pages import page_builder_code


description = 'Verify the application shows error message when code contains error'


def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    index.create_access_project('test')
    api.page.create_access_random_page('test')


def test(data):
    page_code = 'undefined'
    error_message = "Traceback (most recent call last):\nNameError: name 'undefined' is not defined"
    actions.click(page_builder.code_button)
    page_builder_code.set_value(page_code)
    actions.click(page_builder_code.save_button)
    common.assert_toast_message_is_displayed('There are errors in the code')
    page_builder_code.assert_error_message(error_message)
    actions.refresh_page()
    page_builder_code.assert_error_message(error_message)
