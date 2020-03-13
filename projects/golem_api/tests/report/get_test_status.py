from golem import actions

from projects.golem_api.pages import project
from projects.golem_api.pages import report
from projects.golem_api.pages import test_


def setup(data):
    project.using_project('general')
    data.test = project.create_random_test(data.project)
    response = test_.run_test(data.project, data.test)
    actions.store('timestamp', response.json())


def test(data):
    response = report.get_test_status(data.project, data.test, data.timestamp)
    assert response.status_code == 200
