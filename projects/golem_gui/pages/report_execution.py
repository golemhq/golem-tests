import time

from golem.browser import element, elements
from golem import actions


title = ('css', 'h2')
general_table_total_row = ('css', '#generalTable #totalRow', 'General Table Total Row')


def test_row_by_full_test_name(full_test_name):
    return element('#detailTable tr.test-row[test-full-name="{}"]'.format(full_test_name))


def test_detail_row_by_full_test_name(full_test_name):
    return element('#detailTable tr.test-detail-row[test-full-name="{}"]'.format(full_test_name))


def wait_until_execution_end(timeout=30):
    for _ in range(timeout):
        suite_finished = actions.get_browser().execute_script('return ExecutionReport.suiteFinished')
        if suite_finished:
            return
        time.sleep(1)
    raise Exception('Timeout waiting for execution to end')


def assert_amount_of_tests(expected_amount):
    actions.step('Assert number of tests is {}'.format(expected_amount))
    wait_until_execution_end()
    rows = elements('#detailTable > tbody > tr.test-row')
    actual = len(rows)
    assert actual == expected_amount, 'expected {} tests, got {}'.format(expected_amount, actual)


def assert_result_of_test(full_test_name, expected_result):
    """Assert the result of a test by the test full name"""
    test_row = test_row_by_full_test_name(full_test_name)
    result_td = test_row.find('td.test-result')
    actions.assert_element_text_contains(result_td, expected_result)


def expand_test(full_test_name):
    test_row_by_full_test_name(full_test_name).click()
    actions.wait(1)


def assert_test_detail_row_is_displayed(full_test_name):
    detail_row = test_detail_row_by_full_test_name(full_test_name)
    actions.assert_element_displayed(detail_row)


def assert_general_total_row(columns):
    total_row = element(general_table_total_row)
    for column, expected in columns.items():
        if column == 'Total Tests':
            td = total_row.find('td[data="total-tests"]')
        elif column == 'Success':
            td = total_row.find('td[result="success"]')
        elif column == 'Failure':
            td = total_row.find('td[result="failure"]')
        else:
            raise ValueError('{} is an incorrect column value'.format(column))
        msg = 'expected column "{}" to be "{}" but was "{}"'.format(column, expected, td.text)
        assert td.text == expected, msg
