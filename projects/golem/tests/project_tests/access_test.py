
description = 'Verify the user can access a test by clicking on it in the test list.'

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
    store('test_name', 'test_' + random('cccc'))
    project_tests.add_test(data.test_name)
    project_tests.access_test(data.test_name)
    verify_text_in_element(test_builder.test_name, data.test_name)

def teardown(data):
    close()
