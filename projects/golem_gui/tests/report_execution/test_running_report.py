from golem import actions

from projects.golem_gui.pages import common
from projects.golem_gui.pages import api
from projects.golem_gui.pages import urls
from projects.golem_gui.pages import utils
from projects.golem_gui.pages import suite_builder
from projects.golem_gui.pages import report_execution


description = 'Verify an execution is being run'

tags = ['smoke']


def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    api.project.using_project('report_execution')
    data.success_test = utils.create_success_test(data.project)
    data.error_test = utils.create_error_test(data.project)
    data.failing_test = utils.create_failing_test(data.project)
    # create suite with previous tests
    data.suite = api.suite.create_access_suite(data.project, tests=[data.success_test, data.error_test, data.failing_test])


def test(data):
    suite_builder.run_suite()
    suite_builder.access_suite_execution_from_toast()
    report_execution.assert_report_is_running()
    report_execution.wait_until_execution_end()
    report_execution.assert_amount_of_tests(3)
    actions.assert_element_not_displayed(report_execution.main_spinner)
    assert report_execution.get_test_result(data.success_test, 'test_one') == 'success'
    assert report_execution.get_test_result(data.failing_test, 'test_one') == 'failure'
    assert report_execution.get_test_result(data.error_test, 'test_one') == 'error'
    report_execution.assert_general_total_row(columns={'Total Tests': '3', 'Success': '1', 'Failure': '1', 'Error': '1'})
