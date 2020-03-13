from golem import actions

from projects.golem_gui.pages import common
from projects.golem_gui.pages import index
from projects.golem_gui.pages import api
from projects.golem_gui.pages import page_builder
from projects.golem_gui.pages import page_builder_code


description = 'Verify the user can edit page code and save it'

tags = ['smoke']


def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    index.create_access_project('test')
    api.page.create_access_random_page('test')


def test(data):
    page_code = 'test = ("id", "test")'
    actions.click(page_builder.code_button)
    page_builder_code.set_value(page_code)
    page_builder_code.save_page()
    actions.click(page_builder_code.preview_button)
    actions.click(page_builder.code_button)
    page_builder_code.assert_value(page_code)
