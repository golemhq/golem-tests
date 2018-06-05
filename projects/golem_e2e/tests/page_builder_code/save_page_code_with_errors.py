
description = 'Verify the application shows error message when code contains error'

pages = ['common',
         'index',
         'project_pages',
         'page_builder',
         'page_builder_code',
         'code_editor']

def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    index.create_access_project('test')
    common.navigate_menu('Pages')
    project_pages.create_access_random_page()

def test(data):
    store('test_code', 'undefined')
    store('error_message', "Traceback (most recent call last):\nNameError: name 'undefined' is not defined")
    click(page_builder.code_button)
    code_editor.set_value(data.test_code)
    click(page_builder_code.save_button)
    common.verify_toast_message_is_displayed('There are errors in the code')
    page_builder_code.verify_error_message(data.error_message)
    refresh_page()
    page_builder_code.verify_error_message(data.error_message)
