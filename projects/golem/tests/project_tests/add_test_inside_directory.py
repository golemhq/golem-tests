
description = 'Verify that the user can create a new test inside a directory'

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
    store('test_name', random('one/ccccc'))
    project_tests.add_test_directory_if_not_exists('one')
    project_tests.add_test(data.test_name)
    project_tests.verify_test_exists(data.test_name)


def teardown(data):
    close()
