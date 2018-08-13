
description = 'Verify the user can see the code of a page by clicking Code button'

pages = ['common',
         'index',
         'project_pages',
         'page_builder',
         'page_builder_code']

def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    index.create_access_project('test')
    common.navigate_menu('Pages')
    project_pages.create_access_random_page()

def test(data):
    click(page_builder.code_button)
    verify_element_present(page_builder_code.preview_button)
