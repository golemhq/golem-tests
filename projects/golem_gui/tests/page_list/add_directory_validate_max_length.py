
description = 'Verify the length of directory name is validated'

pages = ['common',
         'index',
         'page_list']


def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    index.create_access_project('page_list')
    common.navigate_menu('Pages')


def test(data):
    page_list.add_directory('abcdefghij'*14 + 'a')
    common.assert_error_message('Directory name cannot exceed 140 characters')
