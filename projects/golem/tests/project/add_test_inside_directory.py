
description = 'Verify that the user can create a new test inside a directory'

pages = ['login',
         'index',
         'project']

def setup(data):
    navigate(data.env.url)
    login.do_login('admin', 'admin')
    index.create_access_project('test')

def test(data):
    store('test_name', random('one/ccccc'))
    project.add_test_directory_if_not_exists('one')
    project.add_test(data.test_name)
    project.verify_test_exists(data.test_name)


def teardown(data):
    close()
