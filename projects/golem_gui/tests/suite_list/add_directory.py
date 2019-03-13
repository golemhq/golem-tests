
description = 'Verify the user can add a directory in the suite list view'

pages = ['login',
         'common',
         'index',
         'suite_list']


def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    index.create_access_project('test')


def test(data):
    store('directory_name', 'dir_' + random('cccc'))
    suite_list.add_directory(data.directory_name)
    suite_list.assert_directory_exists(data.directory_name)
