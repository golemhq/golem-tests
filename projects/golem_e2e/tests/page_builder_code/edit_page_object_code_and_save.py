
description = 'Verify the user can edit page code and save it'

pages = ['common',
         'index',
         'project_pages',
         'page_builder',
         'page_builder_code',
         'code_editor']

def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    index.create_access_project('test')
    common.navigate_menu('Pages')
    project_pages.create_access_random_page()

def test(data):
    store('test_code', 'test = ("id", "test")')
    click(page_builder.code_button)
    # code_editor.set_line_value(1, data.test_code)
    code_editor.set_value(data.test_code)
    click(page_builder_code.save_button)
    click(page_builder_code.preview_button)
    click(page_builder.code_button)
    code_editor.assert_value(data.test_code)
