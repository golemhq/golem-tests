
description = 'Verify the user can add an element to a page and save it successfully'

pages = ['common',
         'index',
         'project_pages',
         'page_builder']

def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    index.create_access_project('test')
    common.navigate_menu('Pages')
    project_pages.create_access_random_page()

def test(data):
    store('element_def', ['some_element', 'id', 'selector_value', 'display_name'])
    page_builder.add_element(data.element_def)
    wait(1)
    page_builder.save_page()
    refresh_page()
    page_builder.verify_element_exists(data.element_def)

