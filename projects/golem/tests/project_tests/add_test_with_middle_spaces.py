
description = 'Verify the user can create a test with a name that contains spaces in the middle and they are replaces with underscores'

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
    project_tests.add_test(data.test_name + ' with spaces')
    project_tests.verify_test_exists(data.test_name + '_with_spaces')


def teardown(data):
    close()
