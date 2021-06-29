from golem import actions

from projects.golem_gui.pages import common
from projects.golem_gui.pages import api
from projects.golem_gui.pages import test_builder
from projects.golem_gui.pages import test_run_modal
from projects.golem_gui.pages import test_run_config_modal


description = 'The user can select two environments before running a test'


def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    api.project.create_access_random_project()
    api.project.set_environments(data.project, '{"foo": {}, "bar": {}}')
    api.test.create_access_test(data.project)


def test(data):
    test_builder.open_run_configurations_modal()
    test_run_config_modal.select_env('foo')
    test_run_config_modal.select_env('bar')
    actions.assert_element_attribute(test_run_config_modal.environments_input, 'value', 'foo, bar, ')
    actions.click(test_run_config_modal.run_button)
    test_run_modal.wait_for_test_to_run()
    test_run_modal.assert_amount_of_sets(2)
