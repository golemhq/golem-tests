
description = 'Verify that the user cannot create a new test if a test with the same name already exists'

pages = ['login',
         'index',
         'left_menu',
         'project_tests']

def setup(data):
    navigate(data.env.url)
    login.do_login('admin', 'admin')
    index.create_access_project('test')
    click(left_menu.tests_menu)

def test(data):
    store('test_name', 'test_' + random('cccc'))
    project_tests.add_test(data.test_name)
    project_tests.add_test(data.test_name)
    project_tests.verify_error_message('A test with that name already exists')


def teardown(data):
    close()
