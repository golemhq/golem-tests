
description = 'Verify the application displays a message when page has code errors'

pages = ['common',
         'index',
         'page_list',
         'page_builder',
         'page_builder_code',
         'code_editor']

def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    index.create_access_project('test')
    common.navigate_menu('Pages')
    page_list.create_access_random_page()

def test(data):
    click(page_builder.code_button)
    code_editor.set_value('undefined_var')
    page_builder_code.save_page()
    click(page_builder_code.preview_button)
    assert_page_contains_text('There are errors in the page')
    assert_page_contains_text('There are errors and the page cannot be displayed, open the page code editor to solve them.')
    assert_element_present(page_builder.open_page_code_button)
