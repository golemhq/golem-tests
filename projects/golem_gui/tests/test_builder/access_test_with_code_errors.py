
description = 'Verify the application displays a message when the test has code errors'

pages = ['common',
         'index',
         'test_list',
         'test_builder',
         'test_builder_code',
         'code_editor']

def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    index.create_access_project('test')
    common.navigate_menu('Tests')
    test_list.create_access_random_test()

def test(data):
    click(test_builder.code_button)
    code_editor.set_line_value(0, 'undefined_var')
    test_builder_code.save_test()
    click(test_builder_code.preview_button)
    assert_page_contains_text('There are errors in the test')
    assert_page_contains_text('There are errors and the test cannot be displayed, open the test code editor to solve them.')
    assert_element_present(test_builder.open_test_code_button)
