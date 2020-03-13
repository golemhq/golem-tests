from golem import actions

from projects.golem_api.pages import project
from projects.golem_api.pages import suite
from projects.golem_api.pages import report


def setup(data):
    project.using_project('general')
    data.suite = project.create_random_suite(data.project)
    response = suite.run_suite(data.project, data.suite)
    actions.store('timestamp', response.json())


def test(data):
    response = report.get_suite_execution(data.project, data.suite, data.timestamp)
    assert response.status_code == 200
    assert response.json()['tests'] == []
