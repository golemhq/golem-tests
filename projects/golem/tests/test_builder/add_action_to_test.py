
description = 'Verify that the user can add an action to a test and save it successfully'

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

def test(data):
    project_tests.create_access_test('test_' + random('ccc'))
    test_builder.add_action(data.action)
    test_builder.save_test()
    refresh_page()
    test_builder.verify_last_action(data.action)
