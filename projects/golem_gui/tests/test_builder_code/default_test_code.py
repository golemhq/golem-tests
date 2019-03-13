
description = 'Verify the default test code is correct'

pages = ['common',
         'index',
         'test_list',
         'test_builder',
         'test_builder_code']

def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    index.create_access_project('test')
    common.navigate_menu('Tests')
    test_list.create_access_random_test()
    click(test_builder.code_button)

def test(data):
    test_builder_code.assert_line_value(0, '')
    test_builder_code.assert_line_value(1, 'description = \'\'')
    test_builder_code.assert_line_value(2, '')
    test_builder_code.assert_line_value(3, 'tags = []')
    test_builder_code.assert_line_value(4, '')
    test_builder_code.assert_line_value(5, 'pages = []')
    test_builder_code.assert_line_value(6, '')
    test_builder_code.assert_line_value(7, 'def setup(data):')
    test_builder_code.assert_line_value(8, '    pass')
    test_builder_code.assert_line_value(9, '')
    test_builder_code.assert_line_value(10, 'def test(data):')
    test_builder_code.assert_line_value(11, '    pass')
    test_builder_code.assert_line_value(12, '')
    test_builder_code.assert_line_value(13, 'def teardown(data):')
    test_builder_code.assert_line_value(14, '    pass')
    test_builder_code.assert_line_value(15, '')


