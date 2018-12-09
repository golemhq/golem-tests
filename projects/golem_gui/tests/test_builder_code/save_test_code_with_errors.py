
description = 'Verify the application displays an error message when the user saves test code with errors'

pages = ['common',
         'index',
         'test_list',
         'test_builder',
         'test_builder_code']

def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    index.create_access_project('test')
    common.navigate_menu('Tests')
    store('test_name', 'test_'+random('ddddd'))
    test_list.create_access_test(data.test_name)

def test(data):
    store('page_line', "undefined_var")
    store('error_message', "Traceback (most recent call last):\nNameError: name 'undefined_var' is not defined")
    click(test_builder.code_button)
    test_builder_code.set_value(data.page_line)
    click(test_builder_code.save_button)
    common.assert_toast_message_is_displayed('Test '+data.test_name+' saved')
    common.assert_toast_message_is_displayed('There are errors in the code')
    test_builder_code.assert_error_message(data.error_message)
    refresh_page()
    test_builder_code.assert_error_message(data.error_message)
