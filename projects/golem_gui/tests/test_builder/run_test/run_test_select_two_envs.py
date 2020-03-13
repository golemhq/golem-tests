from golem import actions

from projects.golem_gui.pages import common
from projects.golem_gui.pages import index
from projects.golem_gui.pages import api
from projects.golem_gui.pages import urls
from projects.golem_gui.pages import environments
from projects.golem_gui.pages import test_builder
from projects.golem_gui.pages import test_run_modal
from projects.golem_gui.pages import test_run_config_modal


description = 'The user can select two environments before running a test'


def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    index.create_access_project('project_two_envs')
    actions.navigate(urls.environments('project_two_envs'))
    environments.set_value('{"foo": {}, "bar": {}}')
    actions.click(environments.save_button)
    api.test.create_access_random_test('project_two_envs')


def test(data):
    test_builder.open_run_configurations_modal()
    test_run_config_modal.select_env('foo')
    test_run_config_modal.select_env('bar')
    actions.assert_element_attribute(test_run_config_modal.environments_input, 'value', 'foo, bar, ')
    actions.click(test_run_config_modal.run_button)
    test_run_modal.wait_for_test_to_run()
    test_run_modal.assert_amount_of_sets(2)
