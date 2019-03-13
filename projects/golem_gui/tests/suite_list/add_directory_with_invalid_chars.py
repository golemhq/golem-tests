
description = 'Verify an error is shown when adding a directory with invalid chars'

pages = ['common',
         'index',
         'suite_list']


def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    index.create_access_project('suite_list')


def test(data):
    store('dir_name', 'dir??' + random('dddd'))
    suite_list.add_directory(data.dir_name)
    common.assert_error_message('Only letters, numbers and underscores are allowed')
