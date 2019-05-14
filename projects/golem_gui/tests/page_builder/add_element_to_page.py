
description = 'Verify the user can add an element to a page and save it successfully'

tags = ['smoke']

pages = ['common',
         'index',
         'page_builder',
         'page_list']

def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    index.create_access_project('test')
    common.navigate_menu('Pages')
    page_list.create_access_random_page()

def test(data):
    store('element_def', ['some_element', 'id', 'selector_value', 'display_name'])
    page_builder.add_element(data.element_def)
    page_builder.save_page()
    refresh_page()
    page_builder.assert_element_exists(data.element_def)

def teardown(data):
    pass
