
description = 'Verify the user can create a new page inside a directory'

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
    store('page_name', random('one/ccccc'))
    project_pages.add_page_directory_if_not_exists('one')
    project_pages.add_page(data.page_name)
    project_pages.verify_page_exists(data.page_name)


def teardown(data):
    close()
