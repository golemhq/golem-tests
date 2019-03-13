
description = 'Verify a suite can be duplicated into another directory using dots'

pages = ['common',
         'index',
         'suite_list']


def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    index.create_access_project('suite_list')
    store('suite_name', 'suite' + random('dddd'))
    store('suite_name2', 'dir1.suite' + random('dddd'))
    store('suite_name3', 'dir1.suite' + random('dddd'))
    store('suite_name4', 'suite' + random('dddd'))
    suite_list.add_suite(data.suite_name)
    suite_list.add_suite(data.suite_name2)


def test(data):
    suite_list.duplicate_suite(data.suite_name, data.suite_name3)
    suite_list.assert_suite_exists(data.suite_name3)
    suite_list.duplicate_suite(data.suite_name2, data.suite_name4)
    common.wait_for_toast_to_dissapear()
    suite_list.assert_suite_exists(data.suite_name4)
    refresh_page()
    suite_list.assert_suite_exists(data.suite_name3)
    suite_list.assert_suite_exists(data.suite_name4)
