
description = 'Verify a page can be added to a directory using dots'

pages = ['common',
         'index',
         'page_list']


def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    index.create_access_project('page_list')
    common.navigate_menu('Pages')


def test(data):
    store('dir_name', 'dir' + random('ddddd'))
    store('full_page_name', '{}.{}'.format(data.dir_name, 'page'+random('ddddd')))
    store('full_page_name2', '{}.{}'.format(data.dir_name, 'page'+random('ddddd')))
    # add page to a directory that does not exist using dots
    page_list.add_page(data.full_page_name)
    page_list.assert_directory_exists(data.dir_name)
    page_list.assert_page_exists(data.full_page_name)
    refresh_page()
    page_list.assert_page_exists(data.full_page_name)
    # add page to an existing directory using dots
    page_list.add_page(data.full_page_name2)
    page_list.assert_page_exists(data.full_page_name2)
    refresh_page()
    page_list.assert_page_exists(data.full_page_name2)
    # add page to an existing directory with an existing name
    page_list.add_page(data.full_page_name2)
    common.assert_error_message('A page file with that name already exists')
