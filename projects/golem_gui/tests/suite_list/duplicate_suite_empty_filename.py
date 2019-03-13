
description = 'Verify an error message is displayed when duplicating a suite using an empty name'

pages = ['common',
         'index',
         'suite_list']


def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    index.create_access_project('test')
    common.navigate_menu('Suites')
    store('suite_name', 'suite' + random('dddd'))
    suite_list.add_suite(data.suite_name)


def test(data):
    suite_list.duplicate_suite(data.suite_name, '')
    common.assert_error_message('New filename cannot be empty')