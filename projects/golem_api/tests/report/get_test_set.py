from golem import actions

from projects.golem_api.pages import project
from projects.golem_api.pages import suite
from projects.golem_api.pages import report


def setup(data):
    project.using_project('general')
    data.suite = project.create_random_suite(data.project)
    data.test = project.create_random_test(data.project)
    suite.save_suite(data.project, data.suite, tests=[data.test])
    response = suite.run_suite(data.project, data.suite)
    actions.store('timestamp', response.json())


def test(data):
    report.wait_for_execution_to_finish(data.project, data.suite, data.timestamp)
    response = report.get_suite_execution(data.project, data.suite, data.timestamp)
    test_set = response.json()['tests'][0]['test_set']
    response = report.get_test_set(data.project, data.suite, data.timestamp, data.test, test_set)
    assert response.status_code == 200
    assert response.json()['result'] == 'success'
