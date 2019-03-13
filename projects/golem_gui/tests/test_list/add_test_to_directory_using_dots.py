
description = 'Verify a test can be added to a directory using dots'

pages = ['common',
         'index',
         'test_list']

def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    index.create_access_project('test_list')
    common.navigate_menu('Tests')

def test(data):
    store('dir_name', 'dir' + random('ddddd'))
    store('full_test_name', '{}.{}'.format(data.dir_name, 'test'+random('ddddd')))
    store('full_test_name2', '{}.{}'.format(data.dir_name, 'test'+random('ddddd')))
    # add test to a directory that does not exist using dots
    test_list.add_test(data.full_test_name)
    test_list.assert_directory_exists(data.dir_name)
    test_list.assert_test_exists(data.full_test_name)
    refresh_page()
    test_list.assert_test_exists(data.full_test_name)
    # add test to an existing directory using dots
    test_list.add_test(data.full_test_name2)
    test_list.assert_test_exists(data.full_test_name2)
    refresh_page()
    test_list.assert_test_exists(data.full_test_name2)
    # add test to an existing directory with an existing name
    test_list.add_test(data.full_test_name2)
    common.assert_error_message('A test with that name already exists')
