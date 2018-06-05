
description = 'Verify the user can edit test code and save it'

pages = ['common',
         'index',
         'tests',
         'test_builder',
         'test_builder_code',
         'code_editor']

def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    index.create_access_project('test')
    common.navigate_menu('Tests')
    store('test_name', 'test_'+random('ddddd'))
    tests.create_access_test(data.test_name)

def test(data):
    store('test_line', "description = 'desc'")
    click(test_builder.code_button)
    code_editor.set_line_value(1, data.test_line)
    click(test_builder_code.save_button)
    common.verify_toast_message_is_displayed('Test '+data.test_name+' saved')
    refresh_page()
    code_editor.assert_line_value(1, data.test_line)
