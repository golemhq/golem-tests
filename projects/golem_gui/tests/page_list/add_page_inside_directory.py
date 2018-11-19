
description = 'Verify the user can create a new page inside a directory'

pages = ['login',
         'common',
         'index',
         'page_list']

def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    index.create_access_project('test')
    common.navigate_menu('Pages')

def test(data):
    store('page_name', random('one/ccccc'))
    page_list.add_directory_if_not_exists('one')
    page_list.add_page(data.page_name)
    page_list.assert_page_exists(data.page_name)
