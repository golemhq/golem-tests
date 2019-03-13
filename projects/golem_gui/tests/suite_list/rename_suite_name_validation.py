
description = 'Verify invalid chars and max length is validated when renaming a suite'

pages = ['common',
         'index',
         'suite_list']


def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    index.create_access_project('suite_list')
    store('suite_name', 'suite' + random('dddd'))
    store('long_name', 'abcdefghij' * 14 + 'a')
    suite_list.add_suite(data.suite_name)


def test(data):
    suite_list.rename_suite(data.suite_name, 'suite???')
    common.assert_error_message('Only letters, numbers and underscores are allowed')
    refresh_page()
    suite_list.duplicate_suite(data.suite_name, data.long_name)
    common.assert_error_message('Filename cannot exceed 140 characters')
