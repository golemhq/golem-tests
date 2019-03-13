
description = 'Verify an error is shown when adding a directory with invalid chars'

pages = ['common',
         'index',
         'page_list']


def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    index.create_access_project('page_list')
    common.navigate_menu('Pages')


def test(data):
    store('dir_name', 'dir??' + random('dddd'))
    page_list.add_directory(data.dir_name)
    common.assert_error_message('Only letters, numbers and underscores are allowed')
