
description = 'Verify an error is shown when duplicating a test with an existing name'

pages = ['common',
         'index',
         'test_list']


def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    index.create_access_project('test_list')
    common.navigate_menu('Tests')
    store('test_name', 'test' + random('ddddd'))
    store('test_name2', 'test' + random('ddddd'))
    store('test_name3', 'dir1.test' + random('ddddd'))
    store('test_name4', 'dir1.test' + random('ddddd'))
    test_list.add_test(data.test_name)
    test_list.add_test(data.test_name2)
    test_list.add_test(data.test_name3)
    test_list.add_test(data.test_name4)


def test(data):
    test_list.duplicate_test(data.test_name, data.test_name2)
    common.assert_error_message('A file with that name already exists')
    refresh_page()
    test_list.duplicate_test(data.test_name3, data.test_name4)
    common.assert_error_message('A file with that name already exists')
