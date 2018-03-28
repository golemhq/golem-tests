
description = 'Verify the application displays the correct error message when the page name already exists'

pages = ['login',
         'index',
         'left_menu',
         'project_pages']

def setup(data):
    navigate(data.env.url)
    login.do_login('admin', 'admin')
    index.create_access_project('test')
    click(left_menu.pages_menu)

def test(data):
    store('page_name', 'page_' + random('cccc'))
    project_pages.add_page(data.page_name)
    project_pages.add_page(data.page_name)
    project_pages.verify_error_message('A page file with that name already exists')


def teardown(data):
    close()
