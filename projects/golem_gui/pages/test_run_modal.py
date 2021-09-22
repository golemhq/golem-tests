import time

from golem import actions
from golem.browser import get_browser, element, elements


result_modal_body = ('css', 'div#testRunModal .modal-body #testResultContainer')


def wait_for_test_to_run(timeout=10):
    actions.step('Wait for test to run')
    get_browser().wait_for_element_displayed('#testRunModal', timeout=10)
    selector = '#testRunModal i.fa.fa-cog.fa-spin'
    for _ in range(timeout):
        spinners = elements(selector)
        if not any(x.is_displayed() for x in spinners):
            return
        time.sleep(1)
    raise TimeoutError('waiting for test to finish running')


def assert_result_log_line(index, expected_line):
    # expects one test set
    test_result_logs = elements('#TestRunModalTabContainer>.test-run-tab-content>.test-result-logs>.log-line')
    actual_line = test_result_logs[index].text
    msg = 'Expected "{}" in "{}"'.format(expected_line, actual_line)
    assert expected_line in actual_line, msg


def assert_result(expected_result, test_name='test'):
    # expects one test set
    test_function_report = element(f'//div[@id="testRunModal"]//div[@test-function-name="{test_name}"]')
    result = test_function_report.find('.test-result')
    assert expected_result in result.text


def assert_result_errors(expected_errors):
    # expects one test set
    if not expected_errors:
        assert not get_browser().element_is_present('#testRunModal .error-list')
    else:
        errors = elements('#testRunModal .error-list>li')
        for i, expected_error in enumerate(expected_errors):
            assert errors[i].text == expected_error


def assert_result_steps_is_empty():
    assert not get_browser().element_is_present('#testRunModal .step-list')


def assert_result_steps(expected_steps):
    if not expected_steps:
        assert not get_browser().element_is_present('#testRunModal .step-list')
    else:
        steps = elements('#testRunModal .step-list>li')
        for i, expected_step in enumerate(expected_steps):
            msg = 'Expected step {} to be {} but was {}'.format(i, expected_step, steps[i].text)
            assert steps[i].text == expected_step, msg


def assert_amount_of_sets(amount):
    """Assert that the run modal has the correct
    amount of sets run (tabs)"""
    tabs = elements('#testRunModal .test-run-tab')
    assert len(tabs) == amount, 'expected {} tabs, got {}'.format(amount, len(tabs))