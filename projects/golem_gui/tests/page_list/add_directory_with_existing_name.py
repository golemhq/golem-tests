
description = 'Verify an error is shown when adding a directory with an existing name'

pages = ['common',
         'index',
         'page_list']


def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    index.create_access_project('page_list')
    common.navigate_menu('Pages')


def test(data):
    store('dir_name', 'dir' + random('dddd'))
    page_list.add_directory(data.dir_name)
    page_list.assert_directory_exists(data.dir_name)
    page_list.add_directory(data.dir_name)
    common.assert_error_message('A directory with that name already exists')
    refresh_page()
    store('dir_name2', '{}.{}'.format(data.dir_name, 'dir'+random('dddd')))
    page_list.add_directory(data.dir_name2)
    page_list.assert_directory_exists(data.dir_name2)
    page_list.add_directory(data.dir_name2)
    common.assert_error_message('A directory with that name already exists')
