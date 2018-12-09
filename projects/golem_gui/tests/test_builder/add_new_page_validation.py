
description = 'Verify the the new page modal has validations'

pages = ['common',
         'index',
         'test_list',
         'page_list',
         'test_builder']

def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    index.create_access_project('test_add_page')
    common.navigate_menu('Pages')
    store('page_name', 'page_import_' + random('dddd'))
    page_list.add_page(data.page_name)
    common.navigate_menu('Tests')
    test_list.create_access_random_test()

def test(data):
    step('add a new page with a name that already exists')
    click(test_builder.new_page_button)
    send_keys(test_builder.new_page_modal_input, data.page_name)
    click(test_builder.new_page_modal_submit)
    common.assert_error_message('A page file with that name already exists')
    refresh_page()
    step('add a new page with empty name')
    click(test_builder.new_page_button)
    wait_for_element_displayed(test_builder.new_page_modal_input)
    assert_element_attribute(test_builder.new_page_modal_input, 'value', '')
    click(test_builder.new_page_modal_submit)
    common.assert_error_message('Name cannot be empty')
    refresh_page()
    step('add a new page with invalid characters')
    click(test_builder.new_page_button)
    send_keys(test_builder.new_page_modal_input, '$$invalid')
    click(test_builder.new_page_modal_submit)
    common.assert_error_message("Only letters, numbers, '-' and '_' are allowed")
    refresh_page()
