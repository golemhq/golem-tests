from golem import actions

from projects.golem_api.pages import project
from projects.golem_api.pages import suite
from projects.golem_api.pages import report


def setup(data):
    project.using_project('general')
    data.suite = project.create_random_suite(data.project)
    data.test_name = project.create_random_test(data.project)
    suite.save_suite(data.project, data.suite, tests=[data.test_name])
    response = suite.run_suite(data.project, data.suite)
    actions.store('timestamp', response.json())
    report.wait_for_execution_to_finish(data.project, data.suite, data.timestamp)


def test(data):
    response = report.get_execution(data.project, data.suite, data.timestamp)
    assert response.status_code == 200
    assert response.json()['tests'][0]['test_file'] == data.test_name
    assert response.json()['has_finished'] is True
