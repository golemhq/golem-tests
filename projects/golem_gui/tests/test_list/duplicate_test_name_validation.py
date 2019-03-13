
description = 'Verify the length and valid chars are validated when duplicating a test'

pages = ['common',
         'index',
         'test_list']


def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    index.create_access_project('test_list')
    common.navigate_menu('Tests')
    store('test_name', 'test' + random('ddddd'))
    store('long_name', 'abcdefghij' * 14 + 'a')
    test_list.add_test(data.test_name)


def test(data):
    test_list.duplicate_test(data.test_name, 'new_name??')
    common.assert_error_message('Only letters, numbers and underscores are allowed')
    refresh_page()
    test_list.duplicate_test(data.test_name, data.long_name)
    common.assert_error_message('Filename cannot exceed 140 characters')
