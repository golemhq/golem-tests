import time

import requests

from projects.golem_api.pages.utils import url, headers


TEST_SET_ENDPOINT = '/report/test-set'
LAST_EXECUTIONS_ENDPOINT = '/report/last-executions'
PROJECT_LAST_EXECUTIONS_ENDPOINT = '/report/project/last-executions'
SUITE_LAST_EXECUTIONS_ENDPOINT = '/report/suite/last-executions'
TEST_STATUS_ENDPOINT = '/report/test/status'
SUITE_EXECUTION_ENDPOINT = '/report/suite/execution'
DELETE_EXECUTION_URL = '/report/execution'


def get_test_set(project, suite_name, execution_timestamp, test_name, test_set, user=None):
    params = {
        'project': project,
        'suite': suite_name,
        'execution': execution_timestamp,
        'testName': test_name,
        'testSet': test_set,
    }
    return requests.get(url(TEST_SET_ENDPOINT), headers=headers(user), params=params)


def get_last_executions(user=None):
    return requests.get(url(LAST_EXECUTIONS_ENDPOINT), headers=headers(user))


def get_project_last_executions(project, user=None):
    return requests.get(url(PROJECT_LAST_EXECUTIONS_ENDPOINT), headers=headers(user),
                        params={'project': project})


def get_suite_last_executions(project, suite, user=None):
    params = {'project': project, 'suite': suite}
    return requests.get(url(SUITE_LAST_EXECUTIONS_ENDPOINT), headers=headers(user), params=params)


def get_test_status(project, test_name, timestamp, user=None):
    params = {
        'project': project,
        'test': test_name,
        'timestamp': timestamp
    }
    return requests.get(url(TEST_STATUS_ENDPOINT), headers=headers(user), params=params)


def get_suite_execution(project, suite, execution_timestamp, user=None):
    params = {
        'project': project,
        'suite': suite,
        'execution': execution_timestamp
    }
    return requests.get(url(SUITE_EXECUTION_ENDPOINT), headers=headers(user), params=params)


def delete_execution(project, suite, execution_timestamp, user=None):
    json_ = {
        'project': project,
        'suite': suite,
        'execution': execution_timestamp
    }
    return requests.delete(url(DELETE_EXECUTION_URL), headers=headers(user), json=json_)


def wait_for_execution_to_finish(project, suite, execution_timestamp, timeout=10, user=None):
    for _ in range(timeout):
        response = get_suite_execution(project, suite, execution_timestamp, user)
        if response.json()['has_finished']:
            return
        time.sleep(1)
    raise TimeoutError('timeout waiting for execution to finish')
