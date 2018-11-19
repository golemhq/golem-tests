
description = 'Verify the user can create a new page from the project page'

pages = ['login',
         'common',
         'index',
         'page_list']

def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    index.create_access_project('test')
    common.navigate_menu('Pages')

def test(data):
    store('page_name', 'page_' + random('cccc'))
    store('new_page_name', data.page_name + '_rename')
    page_list.add_page(data.page_name)
    page_list.assert_page_exists(data.page_name)
    page_list.rename_page(data.page_name, data.new_page_name)
    page_list.assert_page_exists(data.new_page_name)
