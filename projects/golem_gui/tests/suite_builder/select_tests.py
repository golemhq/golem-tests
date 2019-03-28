
description = 'Verify tests can be selected'

pages = ['common',
         'index',
         'test_list',
         'settings',
         'suite_list',
         'suite_builder']


def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    index.create_access_project('suite_builder')
    common.navigate_menu('Tests')
    test_list.add_test_if_not_exists('test_001')
    common.navigate_menu('Suites')
    suite_list.create_access_random_suite()


def test(data):
    wait(1)
    suite_builder.assert_test_not_selected('test_001')
    suite_builder.select_test('test_001')
    suite_builder.assert_test_counter(selected=1)
    suite_builder.save_suite()
    refresh_page()
    suite_builder.assert_test_selected('test_001')
