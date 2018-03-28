
description = 'Verify the application displays a toast message when saving a test when there are no unsaved changes'

pages = ['login',
         'index',
         'left_menu',
         'project_tests',
         'test_builder',
         'common']

def setup(data):
    navigate(data.env.url)
    login.do_login('admin', 'admin')
    index.create_access_project('test')
    click(left_menu.tests_menu)
    store('test_name', 'test_' + random('cccc'))
    project_tests.create_access_test(data.test_name)

def test(data):
    test_builder.add_action('click')
    test_builder.save_test()
    refresh_page()
    click(test_builder.save_button)
    common.verify_toast_message_is_displayed('Test '+data.test_name+' saved')
    