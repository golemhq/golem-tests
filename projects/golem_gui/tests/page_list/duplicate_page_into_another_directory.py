
description = 'Verify a page can be duplicated into another directory using dots'

pages = ['common',
         'index',
         'page_list']


def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    index.create_access_project('page_list')
    common.navigate_menu('Pages')
    store('page_name', 'page' + random('dddd'))
    store('page_name2', 'dir1.page' + random('dddd'))
    store('page_name3', 'dir1.page' + random('dddd'))
    store('page_name4', 'page' + random('dddd'))
    page_list.add_page(data.page_name)
    page_list.add_page(data.page_name2)


def test(data):
    page_list.duplicate_page(data.page_name, data.page_name3)
    page_list.assert_page_exists(data.page_name3)
    page_list.duplicate_page(data.page_name2, data.page_name4)
    common.wait_for_toast_to_dissapear()
    page_list.assert_page_exists(data.page_name4)
    refresh_page()
    page_list.assert_page_exists(data.page_name3)
    page_list.assert_page_exists(data.page_name4)
