from golem import actions

from projects.golem_gui.pages import common
from projects.golem_gui.pages import api
from projects.golem_gui.pages import test_builder
from projects.golem_gui.pages import test_run_config_modal
from projects.golem_gui.pages import test_run_modal


description = 'The user can select two browsers before running a test'


def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    api.project.using_project('test_builder_run')
    api.test.create_access_test(data.project)


def test(data):
    test_builder.open_run_configurations_modal()
    actions.assert_element_attribute(test_run_config_modal.browser_input, 'value', 'chrome, ')
    actions.clear_element(test_run_config_modal.browser_input)
    test_run_config_modal.select_browser('chrome')
    test_run_config_modal.select_browser('firefox')
    actions.assert_element_attribute(test_run_config_modal.browser_input, 'value', 'chrome, firefox, ')
    actions.click(test_run_config_modal.run_button)
    test_run_modal.wait_for_test_to_run()
    test_run_modal.assert_amount_of_sets(2)
