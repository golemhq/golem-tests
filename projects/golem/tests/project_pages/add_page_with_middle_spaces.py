
description = 'Verify the user can create a page with a name that contains spaces in the middle and they are replaces with underscores'

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
    project_pages.add_page(data.page_name + ' with spaces')
    wait(3)
    project_pages.verify_page_exists(data.page_name + '_with_spaces')


def teardown(data):
    close()
