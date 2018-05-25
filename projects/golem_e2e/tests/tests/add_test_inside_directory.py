
description = 'Verify the user can create a new test inside a directory'

pages = ['common',
         'index',
         'tests']

def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    index.create_access_project('test')
    common.navigate_menu('Tests')

def test(data):
    store('test_name', random('one/ccccc'))
    tests.add_test_directory_if_not_exists('one')
    tests.add_test(data.test_name)
    tests.verify_test_exists(data.test_name)
