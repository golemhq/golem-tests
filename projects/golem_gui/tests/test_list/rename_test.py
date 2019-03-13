
description = 'Verify the user can rename a test from the test list'

pages = ['common',
         'index',
         'test_list']


def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    index.create_access_project('test_list')
    common.navigate_menu('Tests')
    store('test_name', 'test' + random('ddddd'))
    store('new_test_name', data.test_name + '_rename')
    test_list.add_test(data.test_name)


def test(data):
    test_list.assert_test_exists(data.test_name)
    test_list.rename_test(data.test_name, data.new_test_name)
    assert not test_list.test_exists(data.test_name)
    test_list.assert_test_exists(data.new_test_name)
    refresh_page()
    test_list.assert_test_exists(data.new_test_name)
