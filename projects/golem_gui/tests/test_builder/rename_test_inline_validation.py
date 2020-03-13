from golem import actions

from projects.golem_gui.pages import common
from projects.golem_gui.pages import index
from projects.golem_gui.pages import api
from projects.golem_gui.pages import test_builder


description = 'Verify an error msg is displayed when renaming test inline with empty string, invalid chars and max length'


def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    index.create_access_project('test')
    actions.store('test_name', actions.random_str())
    api.test.create_access_test('test', data.test_name)


def test(data):
    actions.click(test_builder.test_name)
    actions.clear_element(test_builder.test_name_input)
    # press_key(test_builder.test_name_input, 'TAB')
    common.assert_error_message('New filename cannot be empty')
    actions.refresh_page()
    actions.click(test_builder.test_name)
    actions.send_keys(test_builder.test_name_input, 'abcdefghij' * 14 + 'a')
    actions.press_key(test_builder.test_name_input, 'TAB')
    common.assert_error_message('Filename cannot exceed 140 characters')
    actions.refresh_page()
    actions.click(test_builder.test_name)
    actions.send_keys(test_builder.test_name_input, '??')
    actions.press_key(test_builder.test_name_input, 'TAB')
    common.assert_error_message('Only letters, numbers and underscores are allowed')
    actions.refresh_page()
    actions.assert_element_text(test_builder.test_name, data.test_name)
