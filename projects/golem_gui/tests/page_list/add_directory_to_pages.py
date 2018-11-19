
description = 'Verify the user can add a directory in the pages section by appending \'\\\' at the end'

pages = ['login',
         'common',
         'index',
         'page_list']


def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    index.create_access_project('test')
    common.navigate_menu('Pages')

def test(data):
    store('directory_name', 'page_' + random('cccc'))
    page_list.add_directory(data.directory_name)
    page_list.assert_directory_exists(data.directory_name)
