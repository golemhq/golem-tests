
description = 'Verify that the user can create a new page from the project page'

pages = ['login',
         'index',
         'left_menu',
         'project_pages']

def setup(data):
    navigate(data.env.url)
    login.do_login('admin', 'admin')
    index.create_access_project('test_rename')
    click(left_menu.pages_menu)

def test(data):
    store('page_name', 'page_' + random('cccc'))
    store('new_page_name', data.page_name + '_rename')
    project_pages.add_page(data.page_name)
    project_pages.verify_page_exists(data.page_name)
    project_pages.rename_page(data.page_name, data.new_page_name)
    project_pages.verify_page_exists(data.new_page_name)

def teardown(data):
    close()
