
description = 'Verify the length of directory name is validated'

pages = ['common',
         'index',
         'test_builder',
         'suite_list']


def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    index.create_access_project('suite_list')


def test(data):
    suite_list.add_directory('abcdefghij'*14 + 'a')
    common.assert_error_message('Directory name cannot exceed 140 characters')
