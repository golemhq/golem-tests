
description = 'Verify the user can create a new test from the project page'

pages = ['common',
         'index',
         'tests',
         'test_builder']

def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    index.create_access_project('test')
    common.navigate_menu('Tests')

def test(data):
    store('test_name', 'test_' + random('cccc'))
    tests.add_test(data.test_name)
    tests.verify_test_exists(data.test_name)
