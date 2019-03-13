
description = 'Verify a suite can be added to a directory using dots'

pages = ['common',
         'index',
         'suite_list']


def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    index.create_access_project('suite_list')


def test(data):
    store('dir_name', 'dir' + random('ddddd'))
    store('full_suite_name', '{}.{}'.format(data.dir_name, 'suite'+random('ddddd')))
    store('full_suite_name2', '{}.{}'.format(data.dir_name, 'suite'+random('ddddd')))
    # add suite to a directory that does not exist using dots
    suite_list.add_suite(data.full_suite_name)
    suite_list.assert_directory_exists(data.dir_name)
    suite_list.assert_suite_exists(data.full_suite_name)
    refresh_page()
    suite_list.assert_suite_exists(data.full_suite_name)
    # add test to an existing directory using dots
    suite_list.add_suite(data.full_suite_name2)
    suite_list.assert_suite_exists(data.full_suite_name2)
    refresh_page()
    suite_list.assert_suite_exists(data.full_suite_name2)
    # add test to an existing directory with an existing name
    suite_list.add_suite(data.full_suite_name2)
    common.assert_error_message('A suite with that name already exists')
