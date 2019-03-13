
description = 'Verify invalid chars and max length is validated when renaming a test'

pages = ['common',
         'index',
         'test_list']


def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    index.create_access_project('test_list')
    common.navigate_menu('Tests')
    store('test_name', 'test' + random('dddd'))
    store('long_name', 'abcdefghij' * 14 + 'a')
    test_list.add_test(data.test_name)


def test(data):
    test_list.rename_test(data.test_name, 'test???')
    common.assert_error_message('Only letters, numbers and underscores are allowed')
    refresh_page()
    test_list.duplicate_test(data.test_name, data.long_name)
    common.assert_error_message('Filename cannot exceed 140 characters')
