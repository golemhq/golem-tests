from golem import actions

from projects.golem_gui.pages import common
from projects.golem_gui.pages import index
from projects.golem_gui.pages import api
from projects.golem_gui.pages import test_builder
from projects.golem_gui.pages import test_run_config_modal


description = 'The config modal validates: envs exist, processes is a positive integer'


def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    index.create_access_project('test')
    api.test.create_access_random_test('test')


def test(data):
    test_builder.open_run_configurations_modal()
    actions.assert_element_value(test_run_config_modal.processes_input, '1')
    actions.clear_element(test_run_config_modal.processes_input)
    actions.send_keys(test_run_config_modal.processes_input, '0')
    actions.click(test_run_config_modal.run_button)
    common.assert_info_bar_message('Processes must be at least one')
    actions.refresh_page()
    test_builder.open_run_configurations_modal()
    actions.clear_element(test_run_config_modal.processes_input)
    actions.send_keys(test_run_config_modal.processes_input, 'abc')
    actions.click(test_run_config_modal.run_button)
    common.assert_info_bar_message('Processes must be an integer')
    actions.refresh_page()
    test_builder.open_run_configurations_modal()
    actions.send_keys(test_run_config_modal.environments_input, 'not-existent-env')
    actions.click(test_run_config_modal.run_button)
    common.assert_info_bar_message('Environment not-existent-env does not exist for project test')
