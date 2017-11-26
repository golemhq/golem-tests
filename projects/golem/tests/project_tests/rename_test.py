
description = 'Verify that the user can create a new test from the project page'

pages = ['login',
         'index',
         'left_menu',
         'project_tests']

def setup(data):
    navigate(data.env.url)
    login.do_login('admin', 'admin')
    index.create_access_project('test_rename')
    click(left_menu.tests_menu)

def test(data):
    store('test_name', 'test_' + random('cccc'))
    store('new_test_name', data.test_name + '_rename')
    project_tests.add_test(data.test_name)
    project_tests.verify_test_exists(data.test_name)
    project_tests.rename_test(data.test_name, data.new_test_name)
    project_tests.verify_test_exists(data.new_test_name)

def teardown(data):
    close()
