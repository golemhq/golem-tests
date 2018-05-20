
description = 'Verify the user can edit page code and save it'

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
    store('test_code', 'test = ("id", "test")')
    click(page_builder.code_button)
    page_builder_code.write_code(data.test_code)
    click(page_builder_code.save_button)
    click(page_builder_code.preview_button)
    click(page_builder.code_button)
    page_builder_code.verify_page_code(data.test_code)
