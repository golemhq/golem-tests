
description = 'Verify the application displays a message when page has code errors'

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
    click(page_builder.code_button)
    code_editor.set_value('undefined_var')
    click(page_builder_code.save_button)
    click(page_builder_code.preview_button)
    verify_page_contains_text('There are errors in the page')
    verify_page_contains_text('There are errors and the page cannot be displayed, open the page code editor to solve them.')
    # TODO verify Open Page Code button present and click it