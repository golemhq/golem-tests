
description = 'Verify the user can duplicate a test and tags are displayed for duplicated test'

pages = ['common',
         'index',
         'test_list',
         'test_builder']


def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    index.create_access_project('test_list')
    common.navigate_menu('Tests')
    store('test_name', 'test' + random('ddddd'))
    store('new_test_name', data.test_name + 'copy')
    test_list.create_access_test(data.test_name)
    send_keys(test_builder.tags_input, 'foo, bar')
    test_builder.save_test()
    common.navigate_menu('Tests')


def test(data):
    test_list.duplicate_test(data.test_name, data.new_test_name)
    test_list.assert_test_exists(data.test_name)
    test_list.assert_test_exists(data.new_test_name)
    test_list.assert_test_tags(data.new_test_name, ['foo', 'bar'])
