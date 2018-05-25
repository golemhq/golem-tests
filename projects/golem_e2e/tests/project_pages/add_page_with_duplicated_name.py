
description = 'Verify the application displays the correct error message when the page name already exists'

pages = ['login',
         'common',
         'index',
         'project_pages']

def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    index.create_access_project('test')
    common.navigate_menu('Pages')

def test(data):
    store('page_name', 'page_' + random('cccc'))
    project_pages.add_page(data.page_name)
    project_pages.add_page(data.page_name)
    project_pages.verify_error_message('A page file with that name already exists')
