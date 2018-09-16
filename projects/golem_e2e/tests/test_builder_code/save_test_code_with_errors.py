
description = 'Verify the application displays an error message when the user saves test code with errors'

pages = ['common',
         'index',
         'project_tests',
         'test_builder',
         'test_builder_code',
         'code_editor']

def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    index.create_access_project('test')
    common.navigate_menu('Tests')
    store('test_name', 'test_'+random('ddddd'))
    project_tests.create_access_test(data.test_name)

def test(data):
    store('test_line', "undefined_var")
    store('error_message', "Traceback (most recent call last):\nNameError: name 'undefined_var' is not defined")
    click(test_builder.code_button)
    code_editor.set_line_value(0, data.test_line)
    click(test_builder_code.save_button)
    common.verify_toast_message_is_displayed('Test '+data.test_name+' saved')
    common.verify_toast_message_is_displayed('There are errors in the code')
    test_builder_code.verify_error_message(data.error_message)
    refresh_page()
    test_builder_code.verify_error_message(data.error_message)
