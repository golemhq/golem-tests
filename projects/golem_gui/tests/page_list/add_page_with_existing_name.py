
description = 'Verify the user cannot create a new page if a test with the same name exists'

pages = ['common',
         'index',
         'page_list']


def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    index.create_access_project('page_list')
    common.navigate_menu('Pages')


def test(data):
    store('page_name', 'page' + random('dddd'))
    page_list.add_page(data.page_name)
    page_list.add_page(data.page_name)
    common.assert_error_message('A page file with that name already exists')
