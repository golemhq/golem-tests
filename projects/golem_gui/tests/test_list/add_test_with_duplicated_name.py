
description = 'Verify the user cannot create a new test if a test with the same name already exists'

pages = ['common',
         'index',
         'test_list']

def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    index.create_access_project('test')
    common.navigate_menu('Tests')

def test(data):
    store('test_name', 'test_' + random('cccc'))
    test_list.add_test(data.test_name)
    test_list.add_test(data.test_name)
    test_list.assert_error_message('a test with that name already exists')
