
description = 'Verify that the user can access a test by clicking on it in the test list.'

pages = ['login',
         'index',
         'project',
         'test_page']

def setup(data):
    navigate(data.env.url)
    login.do_login('admin', 'admin')
    index.create_access_project('test')

def test(data):
    store('test_name', random('ccccc'))
    project.add_test(data.test_name)
    project.access_test(data.test_name)
    verify_text_in_element(test_page.test_name, data.test_name)

def teardown(data):
    close()
