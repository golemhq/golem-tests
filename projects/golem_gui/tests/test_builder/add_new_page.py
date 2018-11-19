
description = 'Verify the user can import a page into the test'

pages = ['common',
         'index',
         'test_list',
         'test_builder']

def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    index.create_access_project('test')
    common.navigate_menu('Tests')
    test_list.create_access_random_test()

def test(data):
    store('page_name', 'new_page_' + random('dddd')) 
    test_builder.add_new_page(data.page_name)
    test_builder.assert_page_in_list(data.page_name)
