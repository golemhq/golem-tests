from golem import actions

from projects.golem_gui.pages import common
from projects.golem_gui.pages import api
from projects.golem_gui.pages import test_builder


def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    api.project.using_project('test_builder')
    data.test = api.test.create_access_test(data.project)


def test_rename_test_inline_blank(data):
    actions.click(test_builder.test_name)
    actions.clear_element(test_builder.test_name_input)
    common.assert_toast_message_is_displayed('File name cannot be empty')
    actions.refresh_page()
    actions.assert_element_text(test_builder.test_name, data.test)


def test_rename_test_inline_too_long(data):
    actions.refresh_page()
    actions.click(test_builder.test_name)
    actions.send_keys(test_builder.test_name_input, 'abcdefghij' * 14 + 'a')
    actions.press_key(test_builder.test_name_input, 'TAB')
    common.assert_toast_message_is_displayed('Maximum name length is 150 characters')
    actions.refresh_page()
    actions.assert_element_text(test_builder.test_name, data.test)


def test_rename_test_inline_invalid_chars(data):
    actions.refresh_page()
    actions.click(test_builder.test_name)
    actions.send_keys(test_builder.test_name_input, '??')
    actions.press_key(test_builder.test_name_input, 'TAB')
    common.assert_toast_message_is_displayed('Only letters, numbers and underscores are allowed')
    actions.refresh_page()
    actions.assert_element_text(test_builder.test_name, data.test)
