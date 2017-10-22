
description = 'Verify that the user can create a page with a name that contains spaces in the middle and they are replaces with underscores'

pages = ['login',
         'index',
         'project']

def setup(data):
    navigate(data.env.url)
    login.do_login('admin', 'admin')
    index.create_access_project('test')

def test(data):
    store('page_name', random('cccccc'))
    project.add_page(data.page_name + ' with spaces')
    project.verify_page_exists(data.page_name + '_with_spaces')


def teardown(data):
    close()
