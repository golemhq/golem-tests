from golem import actions

from projects.golem_gui.pages import common
from projects.golem_gui.pages import index
from projects.golem_gui.pages import api
from projects.golem_gui.pages import test_builder
from projects.golem_gui.pages import test_builder_common


description = 'Verify the user can add a variable to the datatable'


def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    index.create_access_project('test')
    api.test.create_access_random_test('test')


def test(data):
    test_builder_common.add_variable_to_datatable('foo', ['bar'])
    test_builder.save_test()
    actions.refresh_page()
    test_builder_common.assert_variable_in_datatable('foo')
