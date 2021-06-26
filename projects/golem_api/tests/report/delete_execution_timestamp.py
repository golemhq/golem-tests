from golem import actions

from projects.golem_api.pages import project
from projects.golem_api.pages import suite
from projects.golem_api.pages import report


def setup(data):
    project.using_project('general')
    data.suite_name = project.create_random_suite(data.project)
    response = suite.run_suite(data.project, data.suite_name)
    data.timestamp = response.json()
    report.wait_for_execution_to_finish(data.project, data.suite_name, data.timestamp)


def test_delete_execution_timestamp(data):
    response = report.delete_execution_timestamp(data.project, data.suite_name, data.timestamp)
    assert response.status_code == 200
    assert response.json() == []

    response = report.get_execution_last_executions(data.project, data.suite_name)
    expected = {'projects': {'general': {data.suite_name: []}}}
    assert response.json() == expected


def test_delete_execution_timestamp_does_not_exist(data):
    timestamp = actions.random_str()
    response = report.delete_execution_timestamp(data.project, data.suite_name, timestamp)
    assert response.status_code == 200
    assert response.json() == [
        'Execution for {} {} {} does not exist'.format(data.project, data.suite_name, timestamp)]


def test_delete_execution_execution_does_not_exist(data):
    timestamp = actions.random_str()
    suite_name = actions.random_str()
    response = report.delete_execution_timestamp(data.project, suite_name, timestamp)
    assert response.status_code == 200
    assert response.json() == [
        'Execution for {} {} {} does not exist'.format(data.project, suite_name, timestamp)]