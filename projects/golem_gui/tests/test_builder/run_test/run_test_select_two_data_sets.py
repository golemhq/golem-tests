from golem import actions

from projects.golem_gui.pages import common
from projects.golem_gui.pages import index
from projects.golem_gui.pages import api
from projects.golem_gui.pages import test_builder
from projects.golem_gui.pages import test_run_modal
from projects.golem_gui.pages import test_builder_common


description = 'The user can add two data sets before running a test'


def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    index.create_access_project('project_two_envs')
    api.test.create_access_random_test('project_no_envs')


def test(data):
    test_builder_common.add_variable_to_datatable('foo', ['1', '2'])
    actions.click(test_builder.run_button)
    test_run_modal.wait_for_test_to_run()
    test_run_modal.assert_amount_of_sets(2)
