from golem import actions

from projects.golem_gui.pages import common
from projects.golem_gui.pages import api
from projects.golem_gui.pages import test_builder


description = 'Verify the the new page modal has validations'


def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    api.project.using_project('test_builder')
    api.test.create_access_test(data.project)


def test_add_new_page_name_already_exists(data):
    page_name = api.page.create_page(data.project)
    actions.click(test_builder.new_page_button)
    actions.send_keys(test_builder.new_page_modal_input, page_name)
    actions.click(test_builder.new_page_modal_submit)
    common.assert_error_message('A page with that name already exists')


def test_add_new_page_with_empty_name(data):
    actions.refresh_page()
    actions.click(test_builder.new_page_button)
    actions.wait_for_element_displayed(test_builder.new_page_modal_input)
    actions.assert_element_attribute(test_builder.new_page_modal_input, 'value', '')
    actions.click(test_builder.new_page_modal_submit)
    common.assert_error_message('New filename cannot be empty')


def test_add_new_page_with_invalid_chars(data):
    actions.refresh_page()
    actions.click(test_builder.new_page_button)
    actions.send_keys(test_builder.new_page_modal_input, '$$invalid')
    actions.click(test_builder.new_page_modal_submit)
    common.assert_error_message("Only letters, numbers and underscores are allowed")
    actions.refresh_page()
