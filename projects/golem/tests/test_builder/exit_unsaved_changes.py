
description = 'Verify an alert is displayed when the user leaves the test builder with unsaved changes'

pages = ['login',
         'index',
         'left_menu',
         'project_tests',
         'test_builder']

def setup(data):
    navigate(data.env.url)
    login.do_login('admin', 'admin')
    index.create_access_project('test')
    click(left_menu.tests_menu)
    project_tests.create_access_test('test_' + random('cccc'))

def test(data):
    test_builder.add_action('click')
    refresh_page()
    verify_alert_is_present()
    accept_alert()