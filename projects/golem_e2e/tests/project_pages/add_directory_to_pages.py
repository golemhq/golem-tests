
description = 'Verify the user can add a directory in the pages section by appending \'\\\' at the end'

pages = ['login',
         'common',
         'index',
         'project_pages']


def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    index.create_access_project('test')
    common.navigate_menu('Pages')

def test(data):
    store('directory_name', 'page_' + random('cccc'))
    project_pages.add_page_directory(data.directory_name)
    project_pages.verify_page_directory_exists(data.directory_name)
