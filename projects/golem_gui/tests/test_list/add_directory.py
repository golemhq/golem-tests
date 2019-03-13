
description = 'Verify the user can add a directory to the test list'

pages = ['common',
         'index',
         'test_list']


def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    index.create_access_project('test_list')
    common.navigate_menu('Tests')


def test(data):
    store('dir_name', 'dir' + random('ddddd'))
    test_list.add_directory(data.dir_name)
    test_list.assert_directory_exists(data.dir_name)
