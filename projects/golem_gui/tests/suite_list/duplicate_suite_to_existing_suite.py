
description = 'Verify an error message is displayed when duplicating a suite to a existing filename'

pages = ['common',
         'index',
         'suite_list',
         'suite_builder']


def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    index.create_access_project('suite_list')
    common.navigate_menu('Suites')
    store('suite_one', 'suite' + random('ddddd'))
    store('suite_two', 'suite' + random('ddddd'))
    suite_list.add_suite(data.suite_one)
    suite_list.add_suite(data.suite_two)


def test(data):
    suite_list.duplicate_suite(data.suite_one, data.suite_two)
    common.assert_error_message('A file with that name already exists')
