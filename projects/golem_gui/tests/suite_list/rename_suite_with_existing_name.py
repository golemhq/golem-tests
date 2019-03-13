
description = 'Verify an error is shown when duplicating a suite with existing name'

pages = ['common',
         'index',
         'suite_list']


def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    index.create_access_project('suite_list')
    store('suite_name', 'suite' + random('dddd'))
    store('suite_name2', 'suite' + random('dddd'))
    suite_list.add_suite(data.suite_name)
    suite_list.add_suite(data.suite_name2)


def test(data):
    suite_list.rename_suite(data.suite_name, data.suite_name2)
    common.assert_error_message('A file with that name already exists')
