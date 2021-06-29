from projects.golem_gui.pages import common
from projects.golem_gui.pages import api
from projects.golem_gui.pages import test_builder_code


description = 'Verify the default test code is correct'


def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    api.project.using_project('test_builder_code')
    api.test.create_access_test_code(data.project)


def test(data):
    test_builder_code.assert_line_value(0, '')
    test_builder_code.assert_line_value(1, 'def test(data):')
    test_builder_code.assert_line_value(2, '    pass')
    test_builder_code.assert_line_value(3, '')
