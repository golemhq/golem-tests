
description = 'Verify the suite name is validated'

pages = ['common',
         'index',
         'suite_list']


def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    index.create_access_project('suite_list')


def test(data):
    # invalid chars
    suite_list.add_suite('suite?')
    common.assert_error_message('Only letters, numbers and underscores are allowed')
    refresh_page()
    suite_list.add_suite('suite-suite-suite')
    common.assert_error_message('Only letters, numbers and underscores are allowed')
    assert not suite_list.suite_exists('test-test-test')
    refresh_page()
    # max length
    suite_list.add_suite('abcdefghij'*14 + 'a')
    common.assert_error_message('Filename cannot exceed 140 characters')
