import time

import requests

from projects.golem_api.pages.utils import url, headers


GET_TEST_ENDPOINT = '/report/test'
LAST_EXECUTIONS_ENDPOINT = '/report/last-executions'
PROJECT_LAST_EXECUTIONS_ENDPOINT = '/report/project/last-executions'
SUITE_LAST_EXECUTIONS_ENDPOINT = '/report/suite/last-executions'
TEST_STATUS_ENDPOINT = '/report/test/status'
EXECUTION_ENDPOINT = '/report/execution'
DELETE_EXECUTION_TIMESTAMP_URL = '/report/execution/timestamp'


def get_test(project, execution, timestamp, test_file, test, set_name, user=None):
    params = {
        'project': project,
        'execution': execution,
        'timestamp': timestamp,
        'testFile': test_file,
        'test': test,
        'setName': set_name,
    }
    return requests.get(url(GET_TEST_ENDPOINT), headers=headers(user), params=params)


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


def get_execution(project, execution, timestamp, user=None):
    params = {
        'project': project,
        'execution': execution,
        'timestamp': timestamp
    }
    return requests.get(url(EXECUTION_ENDPOINT), headers=headers(user), params=params)


def delete_execution_timestamp(project, execution, timestamp, user=None):
    json_ = {
        'project': project,
        'execution': execution,
        'timestamp': timestamp
    }
    return requests.delete(url(DELETE_EXECUTION_TIMESTAMP_URL), headers=headers(user), json=json_)


def wait_for_execution_to_finish(project, execution, timestamp, timeout=10, user=None):
    for _ in range(timeout):
        response = get_execution(project, execution, timestamp, user)
        if response.json()['has_finished']:
            return
        time.sleep(1)
    raise TimeoutError('timeout waiting for execution to finish')
