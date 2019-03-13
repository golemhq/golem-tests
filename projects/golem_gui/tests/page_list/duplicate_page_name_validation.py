
description = 'Verify the length and valid chars are validated when duplicating a page'

pages = ['common',
         'index',
         'page_list']


def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    index.create_access_project('page_list')
    common.navigate_menu('Pages')
    store('page_name', 'page' + random('dddd'))
    store('long_name', 'abcdefghij' * 14 + 'a')
    page_list.add_page(data.page_name)


def test(data):
    page_list.duplicate_page(data.page_name, 'new_name??')
    common.assert_error_message('Only letters, numbers and underscores are allowed')
    refresh_page()
    page_list.duplicate_page(data.page_name, data.long_name)
    common.assert_error_message('Filename cannot exceed 140 characters')
