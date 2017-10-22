
description = 'Verify that the user can access a page by clicking on it in the page list.'

pages = ['login',
         'index',
         'project',
         'page_builder']

def setup(data):
    navigate(data.env.url)
    login.do_login('admin', 'admin')
    index.create_access_project('test')

def test(data):
    store('page_name', random('ccccc'))
    project.add_page(data.page_name)
    project.access_page(data.page_name)
    verify_text_in_element(page_builder.page_name, data.page_name)


def teardown(data):
    close()
