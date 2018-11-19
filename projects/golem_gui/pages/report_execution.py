import time

from golem.browser import element, elements
from golem import actions


def wait_until_execution_end(timeout=30):
    for _ in range(timeout):
        suite_finished = actions.get_browser().execute_script('return ExecutionReport.suiteFinished')
        if suite_finished:
            return
        time.sleep(1)
    raise Exception('Timeout waiting for execution to end')


def assert_amount_of_tests(expected_amount):
    wait_until_execution_end()
    rows = elements('#detailTable > tbody > tr')
    actual = len(rows)
    assert actual == expected_amount, 'expected {} tests, got {}'.format(expected_amount, expected_amount)