
description = 'Verify the user can access a page by clicking on it in the page list.'

pages = ['login',
         'index',
         'left_menu',
         'project_pages',
         'page_builder']

def setup(data):
    navigate(data.env.url)
    login.do_login('admin', 'admin')
    index.create_access_project('test')
    click(left_menu.pages_menu)

def test(data):
    store('page_name', 'page_' + random('cccc'))
    project_pages.add_page(data.page_name)
    project_pages.access_page(data.page_name)
    verify_text_in_element(page_builder.page_name, data.page_name)


def teardown(data):
    close()
