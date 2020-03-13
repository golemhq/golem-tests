from golem import actions

from projects.golem_api.pages import project
from projects.golem_api.pages import suite
from projects.golem_api.pages import report


def setup(data):
    project.using_project('general')
    project.create_random_test(data.project)
    response = suite.run_suite(data.project, '.')
    actions.store('timestamp', response.json())


def test(data):
    response = report.delete_execution(data.project, 'all', data.timestamp)
    assert response.status_code == 200
    assert response.json() == []
