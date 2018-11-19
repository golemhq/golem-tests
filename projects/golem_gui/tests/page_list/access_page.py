
description = 'Verify the user can access a page by clicking on it in the page list.'

pages = ['login',
         'common',
         'index',
         'page_list',
         'page_builder']

def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    index.create_access_project('test')
    common.navigate_menu('Pages')

def test(data):
    store('page_name', 'page_' + random('cccc'))
    page_list.add_page(data.page_name)
    page_list.access_page(data.page_name)
    assert_element_text(page_builder.page_name, data.page_name)