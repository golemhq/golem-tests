from golem import actions

from projects.golem_gui.pages import common
from projects.golem_gui.pages import index
from projects.golem_gui.pages import api
from projects.golem_gui.pages import test_builder
from projects.golem_gui.pages import test_builder_code


description = 'Verify the default test code is correct'


def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    index.create_access_project('test')
    api.test.create_access_random_test('test')
    actions.click(test_builder.code_button)


def test(data):
    test_builder_code.assert_line_value(0, '')
    test_builder_code.assert_line_value(1, 'description = \'\'')
    test_builder_code.assert_line_value(2, '')
    test_builder_code.assert_line_value(3, 'tags = []')
    test_builder_code.assert_line_value(4, '')
    test_builder_code.assert_line_value(5, 'pages = []')
    test_builder_code.assert_line_value(6, '')
    test_builder_code.assert_line_value(7, '')
    test_builder_code.assert_line_value(8, 'def setup(data):')
    test_builder_code.assert_line_value(9, '    pass')
    test_builder_code.assert_line_value(10, '')
    test_builder_code.assert_line_value(11, '')
    test_builder_code.assert_line_value(12, 'def test(data):')
    test_builder_code.assert_line_value(13, '    pass')
    test_builder_code.assert_line_value(14, '')
    test_builder_code.assert_line_value(15, '')
    test_builder_code.assert_line_value(16, 'def teardown(data):')
    test_builder_code.assert_line_value(17, '    pass')
    test_builder_code.assert_line_value(18, '')
