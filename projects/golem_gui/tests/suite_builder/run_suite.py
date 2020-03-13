from golem import actions

from projects.golem_gui.pages import common
from projects.golem_gui.pages import index
from projects.golem_gui.pages import api
from projects.golem_gui.pages import suite_builder
from projects.golem_gui.pages import report_execution


description = 'Run a suite'

tags = ['smoke']


def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    index.create_access_project('run_suite')
    api.test.create_test('run_suite', 'test_one')
    api.test.create_test('run_suite', 'test_two')
    actions.store('suite_name', actions.random_str())
    api.suite.create_access_suite('run_suite', data.suite_name)


def test(data):
    suite_builder.select_test('test_one')
    suite_builder.select_test('test_two')
    suite_builder.save_suite()
    actions.click(suite_builder.run_suite_button)
    suite_builder.assert_suite_was_run(data.suite_name)
    suite_builder.access_suite_execution_from_toast()
    report_execution.wait_until_execution_end()
    report_execution.assert_amount_of_tests(2)
