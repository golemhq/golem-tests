
description = 'Verify the application displays the correct error message when the page name already exists'

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
    page_list.add_page(data.page_name)
    page_list.add_page(data.page_name)
    page_list.assert_error_message('A page file with that name already exists')
