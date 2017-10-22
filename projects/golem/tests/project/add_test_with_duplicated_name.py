
description = 'Verify that the user cannot create a new test if a test with the same name already exists'

pages = ['login',
         'index',
         'project']

def setup(data):
    navigate(data.env.url)
    login.do_login('admin', 'admin')

def test(data):
    index.create_access_project('test')
    store('test_name', random('ccccc'))
    project.add_test(data.test_name)
    project.add_test(data.test_name)
    project.verify_error_message('A test with that name already exists')


def teardown(data):
    close()
