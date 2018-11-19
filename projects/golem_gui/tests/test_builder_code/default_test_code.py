
description = 'Verify the default test code is correct'

pages = ['common',
         'index',
         'test_list',
         'test_builder',
         'code_editor']

def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    index.create_access_project('test')
    common.navigate_menu('Tests')
    test_list.create_access_random_test()
    click(test_builder.code_button)

def test(data):
    code_editor.assert_line_value(0, '')
    code_editor.assert_line_value(1, 'description = \'\'')
    code_editor.assert_line_value(2, '')
    code_editor.assert_line_value(3, 'pages = []')
    code_editor.assert_line_value(4, '')
    code_editor.assert_line_value(5, 'def setup(data):')
    code_editor.assert_line_value(6, '    pass')
    code_editor.assert_line_value(7, '')
    code_editor.assert_line_value(8, 'def test(data):')
    code_editor.assert_line_value(9, '    pass')
    code_editor.assert_line_value(10, '')
    code_editor.assert_line_value(11, 'def teardown(data):')
    code_editor.assert_line_value(12, '    pass')
    code_editor.assert_line_value(13, '')


