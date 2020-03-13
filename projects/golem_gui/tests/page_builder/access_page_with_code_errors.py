from golem import actions

from projects.golem_gui.pages import common
from projects.golem_gui.pages import index
from projects.golem_gui.pages import api
from projects.golem_gui.pages import page_builder
from projects.golem_gui.pages import page_builder_code


description = 'Verify the application displays a message when page has code errors'


def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    index.create_access_project('test')
    api.page.create_access_random_page('test')


def test(data):
    actions.click(page_builder.code_button)
    page_builder_code.set_value('undefined_var')
    page_builder_code.save_page()
    actions.click(page_builder_code.preview_button)
    actions.assert_page_contains_text('There are errors in the page')
    actions.assert_page_contains_text('There are errors and the page cannot be displayed, '
                                      'open the page code editor to solve them.')
    actions.assert_element_present(page_builder.open_page_code_button)
