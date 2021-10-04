from golem import actions

from projects.golem_gui.pages import common
from projects.golem_gui.pages import api
from projects.golem_gui.pages import test_builder
from projects.golem_gui.pages import test_builder_code


description = 'Verify the application displays a message when the test has code errors'


def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    api.project.using_project('test_builder')
    api.test.create_access_test(data.project)


def test(data):
    test_builder.go_to_code_view()
    test_builder_code.set_value('undefined_var')
    test_builder_code.save_test()
    test_builder_code.go_to_preview_view()
    actions.assert_page_contains_text('There are errors in the test')
    actions.assert_page_contains_text('There are errors and the test cannot be displayed, open the test code editor to solve them.')
    actions.assert_element_present(test_builder.open_test_code_button)
