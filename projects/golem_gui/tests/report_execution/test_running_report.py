
description = 'Verify an execution is being run'


pages = ['common',
         'index',
         'utils',
         'test_list',
         'suite_builder',
         'report_execution']


def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    index.create_access_project('test_reports')
    store('suite_name', 'suite00001')
    utils.create_access_suite_with_different_results(data.suite_name)


def test(data):
    suite_builder.run_suite()
    suite_builder.access_suite_execution_from_toast()
    report_execution.assert_report_is_running()
    report_execution.wait_until_execution_end()
    report_execution.assert_amount_of_tests(3)
    assert_element_not_displayed(report_execution.main_spinner)
    report_execution.assert_result_of_test('success_test', 'success')
    report_execution.assert_result_of_test('failing_test', 'failure')
    report_execution.assert_result_of_test('error_test', 'error')
    report_execution.assert_general_total_row(columns={'Total Tests': '3', 'Success': '1', 'Failure': '1', 'Error': '1'})
