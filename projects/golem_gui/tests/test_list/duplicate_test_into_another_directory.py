
description = 'Verify a test can be duplicated into another directory using dots'

pages = ['common',
         'index',
         'test_list']


def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    index.create_access_project('test_list')
    common.navigate_menu('Tests')
    store('test_name', 'test' + random('ddddd'))
    store('test_name2', 'pagedir.test' + random('ddddd'))
    store('test_name3', 'pagedir.test' + random('ddddd'))
    store('test_name4', 'test' + random('ddddd'))
    test_list.add_test(data.test_name)
    test_list.add_test(data.test_name2)


def test(data):
    test_list.duplicate_test(data.test_name, data.test_name3)
    test_list.assert_test_exists(data.test_name3)
    test_list.duplicate_test(data.test_name2, data.test_name4)
    test_list.assert_test_exists(data.test_name4)
    refresh_page()
    test_list.assert_test_exists(data.test_name3)
    test_list.assert_test_exists(data.test_name4)
