
description = 'Verify that the user can add a directory in the pages section by appending \'\\\' at the end'

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
    store('directory_name', 'page_' + random('cccc'))
    project_pages.add_page_directory(data.directory_name)
    project_pages.verify_page_directory_exists(data.directory_name)


def teardown(data):
    close()
