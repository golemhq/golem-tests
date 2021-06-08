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
    report.wait_for_execution_to_finish(data.project, data.suite, data.timestamp)


def test(data):
    response = report.get_execution(data.project, data.suite, data.timestamp)
    test_file = response.json()['tests'][0]['test_file']
    test_name = response.json()['tests'][0]['test']
    set_name = response.json()['tests'][0]['set_name']
    response = report.get_test(data.project, data.suite, data.timestamp, test_file,
                               test_name, set_name)
    assert response.status_code == 200
    assert response.json()['result'] == 'success'
    assert response.json()['has_finished'] is True
    assert response.json()['browser'] == 'chrome'
