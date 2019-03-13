
description = 'Verify the test name is validated when adding a test'

pages = ['common',
         'index',
         'test_list']


def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    index.create_access_project('test_list')
    common.navigate_menu('Tests')


def test(data):
    # invalid chars
    test_list.add_test('test?')
    common.assert_error_message('Only letters, numbers and underscores are allowed')
    refresh_page()
    test_list.add_test('test-test-test')
    common.assert_error_message('Only letters, numbers and underscores are allowed')
    assert not test_list.test_exists('test-test-test')
    refresh_page()
    # max length
    test_list.add_test('abcdefghij'*14 + 'a')
    common.assert_error_message('Filename cannot exceed 140 characters')
