
description = 'Verify the application displays a message when the test has code errors'

pages = ['common',
         'index',
         'project_tests',
         'test_builder',
         'test_builder_code',
         'code_editor']

def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    index.create_access_project('test')
    common.navigate_menu('Tests')
    project_tests.create_access_random_test()

def test(data):
    click(test_builder.code_button)
    code_editor.set_line_value(0, 'undefined_var')
    click(test_builder_code.save_button)
    click(test_builder_code.preview_button)
    verify_page_contains_text('There are errors in the test')
    verify_page_contains_text('There are errors and the test cannot be displayed, open the test code editor to solve them.')
    # TODO verify Open Test Code button present and click it
