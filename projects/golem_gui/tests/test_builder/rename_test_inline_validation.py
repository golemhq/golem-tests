
description = 'Verify an error msg is displayed when renaming test inline with empty string, invalid chars and max length'

pages = ['common',
         'index',
         'test_list',
         'test_builder']


def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    index.create_access_project('test_builder')
    common.navigate_menu('Tests')
    store('test_name', 'test'+random('dddd'))
    test_list.create_access_test(data.test_name)


def test(data):
    click(test_builder.test_name)
    clear_element(test_builder.test_name_input)
    # press_key(test_builder.test_name_input, 'TAB')
    common.assert_error_message('New filename cannot be empty')
    refresh_page()
    click(test_builder.test_name)
    send_keys(test_builder.test_name_input, 'abcdefghij' * 14 + 'a')
    press_key(test_builder.test_name_input, 'TAB')
    common.assert_error_message('Filename cannot exceed 140 characters')
    refresh_page()
    click(test_builder.test_name)
    send_keys(test_builder.test_name_input, '??')
    press_key(test_builder.test_name_input, 'TAB')
    common.assert_error_message('Only letters, numbers and underscores are allowed')
    refresh_page()
    assert_element_text(test_builder.test_name, data.test_name)
