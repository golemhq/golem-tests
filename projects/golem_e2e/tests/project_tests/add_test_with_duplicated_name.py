
description = 'Verify the user cannot create a new test if a test with the same name already exists'

pages = ['common',
         'index',
         'project_tests']

def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    index.create_access_project('test')
    common.navigate_menu('Tests')

def test(data):
    store('test_name', 'test_' + random('cccc'))
    tests.add_test(data.test_name)
    tests.add_test(data.test_name)
    tests.verify_error_message('a test with that name already exists')
