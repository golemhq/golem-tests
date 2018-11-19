
description = 'Verify the user can create a test with a name that contains spaces in the middle and they are replaces with underscores'

pages = ['common',
         'index',
         'test_list']

def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    index.create_access_project('test')
    common.navigate_menu('Tests')

def test(data):
    store('test_name', 'test_' + random('cccc'))
    test_list.add_test(data.test_name + ' with spaces')
    test_list.assert_test_exists(data.test_name + '_with_spaces')
