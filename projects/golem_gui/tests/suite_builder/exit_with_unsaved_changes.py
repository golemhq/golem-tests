from golem import actions

from projects.golem_gui.pages import common
from projects.golem_gui.pages import index
from projects.golem_gui.pages import api
from projects.golem_gui.pages import suite_builder


description = 'Verify an alert is shown when exiting suite builder with unsaved changes'


def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    index.create_access_project('test')
    api.suite.create_access_random_suite('test')


def test(data):
    actions.wait(2)
    # actions.clear_element(suite_builder.processes_input)
    actions.check_element(suite_builder.all_tests_checkbox)
    actions.send_keys(suite_builder.processes_input, 3)
    actions.refresh_page()
    actions.wait(2)
    actions.assert_alert_present()
    actions.accept_alert()
    actions.assert_element_value(suite_builder.processes_input, '1')
    actions.clear_element(suite_builder.processes_input)
    actions.send_keys(suite_builder.processes_input, 3)
    actions.refresh_page()
    actions.assert_alert_present()
    actions.dismiss_alert()
    suite_builder.save_suite()
    common.navigate_menu('Suites')
    actions.assert_title_contains(': Suites')
