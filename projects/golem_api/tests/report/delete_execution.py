from golem import actions

from projects.golem_api.pages import project
from projects.golem_api.pages import suite
from projects.golem_api.pages import report


def setup(data):
    project.using_project('general')


def test_delete_execution(data):
    suite_name = project.create_random_suite(data.project)
    response = suite.run_suite(data.project, suite_name)
    timestamp = response.json()
    report.wait_for_execution_to_finish(data.project, suite_name, timestamp)

    response = report.delete_execution(data.project, suite_name)
    assert response.status_code == 200
    assert response.json() == []

    response = report.get_execution_last_executions(data.project, suite_name)
    expected = {'projects': {'general': {}}}
    assert response.json() == expected


def test_delete_execution_does_not_exist(data):
    suite_name = actions.random_str()
    response = report.delete_execution(data.project, suite_name)
    assert response.status_code == 200
    assert response.json() == [
        'Execution {} of project {} does not exist'.format(suite_name, data.project)]
