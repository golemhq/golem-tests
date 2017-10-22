
description = 'Verify that the user can create a test with a name that contains spaces in the middle and they are replaces with underscores'

pages = ['login',
         'index',
         'project']

def setup(data):
    navigate(data.env.url)
    login.do_login('admin', 'admin')
    index.create_access_project('test')

def test(data):
    store('test_name', random('cccccc'))
    project.add_test(data.test_name + ' with spaces')
    project.verify_test_exists(data.test_name + '_with_spaces')


def teardown(data):
    close()
