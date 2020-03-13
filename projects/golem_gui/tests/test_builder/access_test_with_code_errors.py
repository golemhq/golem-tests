from golem import actions

from projects.golem_gui.pages import common
from projects.golem_gui.pages import index
from projects.golem_gui.pages import api
from projects.golem_gui.pages import test_builder
from projects.golem_gui.pages import test_builder_code


description = 'Verify the application displays a message when the test has code errors'


def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    index.create_access_project('test')
    api.test.create_access_random_test('test')


def test(data):
    actions.click(test_builder.code_button)
    test_builder_code.set_value('undefined_var')
    test_builder_code.save_test()
    actions.click(test_builder_code.preview_button)
    actions.assert_page_contains_text('There are errors in the test')
    actions.assert_page_contains_text('There are errors and the test cannot be displayed, open the test code editor to solve them.')
    actions.assert_element_present(test_builder.open_test_code_button)
