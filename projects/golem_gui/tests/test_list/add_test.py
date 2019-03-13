
description = 'Verify the user can create a new test from the project page'

pages = ['common',
         'index',
         'test_builder',
         'test_list']

def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    index.create_access_project('test_list')
    common.navigate_menu('Tests')

def test(data):
    store('test_name', 'test_' + random('cccc'))
    test_list.add_test(data.test_name)
    test_list.assert_test_exists(data.test_name)
