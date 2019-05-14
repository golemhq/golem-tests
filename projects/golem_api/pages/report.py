import time

import requests

from golem import execution

from projects.golem_api.pages import utils


TEST_SET_ENDPOINT = 'api/report/test-set'
SUITE_LAST_EXECUTIONS_ENDPOINT = 'api/report/suite/last-executions'
TEST_STATUS_ENDPOINT = 'api/report/test/status'
SUITE_EXECUTION_ENDPOINT = 'api/report/suite/execution'


def test_set_url(base_url):
    return '{}{}'.format(base_url, TEST_SET_ENDPOINT)


def suite_last_executions_url(base_url):
    return '{}{}'.format(base_url, SUITE_LAST_EXECUTIONS_ENDPOINT)


def test_status_url(base_url):
    return '{}{}'.format(base_url, TEST_STATUS_ENDPOINT)


def suite_execution_url(base_url):
    return '{}{}'.format(base_url, SUITE_EXECUTION_ENDPOINT)


def get_test_set(project, suite_name, execution_timestamp, test_name, test_set, user=None):
    params = {
        'project': project,
        'suite': suite_name,
        'execution': execution_timestamp,
        'testName': test_name,
        'testSet': test_set,
    }
    return requests.get(test_set_url(execution.data.env.url),
                        headers=utils.common_headers(user), params=params)


def get_suite_last_executions(projects, suite, limit, user=None):
    json_ = {
        'projects': projects,
        'suite': suite,
        'limit': limit
    }
    return requests.post(suite_last_executions_url(execution.data.env.url),
                         headers=utils.common_headers(user), json=json_)


def get_test_status(project, test_name, timestamp, user=None):
    params = {
        'project': project,
        'test': test_name,
        'timestamp': timestamp
    }
    return requests.get(test_status_url(execution.data.env.url),
                        headers=utils.common_headers(user), params=params)


def get_suite_execution(project, suite, execution_timestamp, user=None):
    params = {
        'project': project,
        'suite': suite,
        'execution': execution_timestamp
    }
    return requests.get(suite_execution_url(execution.data.env.url),
                        headers=utils.common_headers(user), params=params)


def wait_for_execution_to_finish(project, suite, execution_timestamp, timeout=10, user=None):
    for _ in range(timeout):
        response = get_suite_execution(project, suite, execution_timestamp, user)
        if response.json()['has_finished']:
            return
        time.sleep(1)
    raise TimeoutError('timeout waiting for execution to finish')
