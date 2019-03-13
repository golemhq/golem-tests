
description = 'Verify an error is shown when duplicating a page with an existing name'

pages = ['common',
         'index',
         'page_list']


def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    index.create_access_project('page_list')
    common.navigate_menu('Pages')
    store('page_name', 'page' + random('dddd'))
    store('page_name2', 'page' + random('dddd'))
    store('page_name3', 'dir1.page' + random('dddd'))
    store('page_name4', 'dir1.page' + random('dddd'))
    page_list.add_page(data.page_name)
    page_list.add_page(data.page_name2)
    page_list.add_page(data.page_name3)
    page_list.add_page(data.page_name4)


def test(data):
    page_list.duplicate_page(data.page_name, data.page_name2)
    common.assert_error_message('A file with that name already exists')
    refresh_page()
    page_list.duplicate_page(data.page_name3, data.page_name4)
    common.assert_error_message('A file with that name already exists')
