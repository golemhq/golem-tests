
description = 'Verify the user can create a new test from the project page'

pages = ['common',
         'index',
         'test_list']

def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    index.create_access_project('test')
    common.navigate_menu('Tests')

def test(data):
    store('test_name', 'test_' + random('cccc'))
    store('new_test_name', data.test_name + '_rename')
    test_list.add_test(data.test_name)
    test_list.assert_test_exists(data.test_name)
    test_list.rename_test(data.test_name, data.new_test_name)
    test_list.assert_test_exists(data.new_test_name)
