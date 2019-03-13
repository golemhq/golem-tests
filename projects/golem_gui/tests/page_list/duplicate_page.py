
description = 'Verify the user can duplicate a page and tags are displayed for duplicated test'

pages = ['common',
         'index',
         'page_list']


def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    index.create_access_project('page_list')
    common.navigate_menu('Pages')
    store('page_name', 'page' + random('dddd'))
    store('new_page_name', data.page_name + 'copy')
    page_list.add_page(data.page_name)


def test(data):
    page_list.duplicate_page(data.page_name, data.new_page_name)
    page_list.assert_page_exists(data.page_name)
    page_list.assert_page_exists(data.new_page_name)
