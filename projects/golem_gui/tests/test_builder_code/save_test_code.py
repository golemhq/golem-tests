
description = 'Verify the user can edit test code and save it'

tags = ['smoke']

pages = ['common',
         'index',
         'test_builder',
         'test_list',
         'test_builder_code']

def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    index.create_access_project('test')
    common.navigate_menu('Tests')
    store('test_name', 'test_'+random('ddddd'))
    test_list.create_access_test(data.test_name)

def test(data):
    store('test_line', "description = 'desc'")
    click(test_builder.code_button)
    test_builder_code.set_value(data.test_line)
    click(test_builder_code.save_button)
    common.assert_toast_message_is_displayed('Test '+data.test_name+' saved')
    refresh_page()
    test_builder_code.assert_value(data.test_line)

