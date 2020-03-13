from golem import actions

from projects.golem_gui.pages import common
from projects.golem_gui.pages import index
from projects.golem_gui.pages import api
from projects.golem_gui.pages import suite_builder
from projects.golem_gui.pages import report_execution


description = 'The suite is saved when running with unsaved changes'


def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    actions.store('test', actions.random_str())
    index.create_access_project(data.test)
    api.test.create_test(data.test, 'test_one')
    actions.store('suite_name', actions.random_str())
    api.suite.create_access_suite(data.test, data.suite_name)


def test(data):
    suite_builder.select_test('test_one')
    actions.click(suite_builder.run_suite_button)
    suite_builder.assert_suite_was_run(data.suite_name)
    suite_builder.access_suite_execution_from_toast()
    report_execution.wait_until_execution_end()
    report_execution.assert_amount_of_tests(1)
