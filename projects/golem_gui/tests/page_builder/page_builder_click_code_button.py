from golem import actions

from projects.golem_gui.pages import common
from projects.golem_gui.pages import index
from projects.golem_gui.pages import api
from projects.golem_gui.pages import page_builder
from projects.golem_gui.pages import page_builder_code


description = 'Verify the user can see the code of a page by clicking Code button'


def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    index.create_access_project('test')
    api.page.create_access_random_page('test')


def test(data):
    actions.click(page_builder.code_button)
    actions.assert_element_present(page_builder_code.preview_button)
    actions.assert_url_contains('/code/')
