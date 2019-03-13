
description = 'Verify the user can create a new suite inside a directory'

pages = ['common',
         'index',
         'suite_list']


def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    index.create_access_project('suite_list')


def test(data):
    store('suite_name', random('one.ccccc'))
    suite_list.add_directory_if_not_exists('one')
    suite_list.add_suite(data.suite_name)
    suite_list.assert_suite_exists(data.suite_name)
