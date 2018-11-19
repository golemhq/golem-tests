import time

from golem.browser import element, elements


def wait_until_execution_end(timeout=30):
    # TODO use a timeout manager
    for _ in range(timeout*2):
        total_tests_text = element('#totalRow .total-project_tests').text
        total_tests = int(total_tests_text) if total_tests_text else 99
        total_ok_text = element('#totalRow .project_tests-ok').text
        total_ok = int(total_ok_text) if total_ok_text else 0
        total_failed_text = element('#totalRow .project_tests-failed').text
        total_failed = int(total_failed_text) if total_failed_text else 0
        if total_tests == total_ok + total_failed:
            return
        time.sleep(0.5)
    assert False, 'Timeout waiting for execution to end'


def verify_amount_of_tests(expected_amount):
    wait_until_execution_end()
    rows = elements('#detailTable > tbody > tr')
    assert len(rows) == expected_amount