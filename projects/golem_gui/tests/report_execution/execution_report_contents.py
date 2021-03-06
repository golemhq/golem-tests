from golem import actions

from projects.golem_gui.pages import common
from projects.golem_gui.pages import index
from projects.golem_gui.pages import utils
from projects.golem_gui.pages import suite_builder
from projects.golem_gui.pages import report_execution


description = 'Verify that the user can access the execution report'


def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    index.create_access_project('test_reports')
    actions.store('test_name', 'simple_test')
    utils.create_access_simple_suite('simple_suite01', data.test_name)


def test(data):
    suite_builder.run_suite()
    suite_builder.access_suite_execution_from_toast()
    report_execution.wait_until_execution_end()
    actions.assert_element_text_contains(report_execution.title, 'test reports - simple suite')
    report_execution.assert_amount_of_tests(1)
    report_execution.assert_result_of_test(data.test_name, 'success')
    report_execution.expand_test(data.test_name)
    report_execution.assert_test_detail_row_is_displayed(data.test_name)
    report_execution.assert_general_total_row(columns={'Total Tests': '1', 'Success': '1', 'Failure': '0'})
