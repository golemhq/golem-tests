from golem import actions

from projects.golem_gui.pages import common
from projects.golem_gui.pages import index
from projects.golem_gui.pages import api
from projects.golem_gui.pages import test_builder
from projects.golem_gui.pages import test_builder_code


description = 'Verify the test code page opens when clicking Code button'


def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    index.create_access_project('test')
    api.test.create_access_random_test('test')


def test(data):
    actions.click(test_builder.code_button)
    actions.verify_element_present(test_builder_code.preview_button)
