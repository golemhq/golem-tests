from golem import actions

from projects.golem_gui.pages import common
from projects.golem_gui.pages import index
from projects.golem_gui.pages import api
from projects.golem_gui.pages import test_builder


description = 'Verify the the new page modal has validations'


def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    index.create_access_project('test_add_page')
    actions.store('page_name', actions.random_str())
    api.page.create_page('test_add_page', data.page_name)
    api.test.create_access_random_test('test_add_page')


def test(data):
    # page already exists
    actions.click(test_builder.new_page_button)
    actions.send_keys(test_builder.new_page_modal_input, data.page_name)
    actions.click(test_builder.new_page_modal_submit)
    common.assert_error_message('A page with that name already exists')
    actions.refresh_page()
    # empty name
    actions.click(test_builder.new_page_button)
    actions.wait_for_element_displayed(test_builder.new_page_modal_input)
    actions.assert_element_attribute(test_builder.new_page_modal_input, 'value', '')
    actions.click(test_builder.new_page_modal_submit)
    common.assert_error_message('New filename cannot be empty')
    actions.refresh_page()
    # invalid chars
    actions.click(test_builder.new_page_button)
    actions.send_keys(test_builder.new_page_modal_input, '$$invalid')
    actions.click(test_builder.new_page_modal_submit)
    common.assert_error_message("Only letters, numbers and underscores are allowed")
    actions.refresh_page()
