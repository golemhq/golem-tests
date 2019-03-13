
description = 'Verify the page name is validated'

pages = ['common',
         'index',
         'page_list']


def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    index.create_access_project('page_list')
    common.navigate_menu('Pages')


def test(data):
    # invalid chars
    page_list.add_page('page?')
    common.assert_error_message('Only letters, numbers and underscores are allowed')
    refresh_page()
    page_list.add_page('page-page-page')
    common.assert_error_message('Only letters, numbers and underscores are allowed')
    assert not page_list.page_exists('page-page-page')
    refresh_page()
    # max length
    page_list.add_page('abcdefghij'*14 + 'a')
    common.assert_error_message('Filename cannot exceed 140 characters')
