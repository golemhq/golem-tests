
description = 'Verify the user can import a page into the test'

pages = ['common',
         'index',
         'tests',
         'project_pages',
         'test_builder']

def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    index.create_access_project('test')
    common.navigate_menu('Pages')
    store('page_name', 'page_import_' + random('dddd'))
    project_pages.add_page(data.page_name)
    common.navigate_menu('Tests')
    tests.create_access_random_test()

def test(data):
    test_builder.import_page(data.page_name)
    test_builder.verify_page_in_list(data.page_name)
