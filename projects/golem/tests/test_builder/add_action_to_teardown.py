
description = 'Verify the user can add an action to the teardown'

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
    test_builder.add_action('click', where='teardown')
    test_builder.save_test()
    refresh_page()
    test_builder.verify_last_action('click', where='teardown')
