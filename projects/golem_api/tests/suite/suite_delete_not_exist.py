from projects.golem_api.pages import project
from projects.golem_api.pages import suite


def setup(data):
    project.using_project('general')


def test(data):
    response = suite.delete_suite(data.project, 'suite_not_exists')
    assert response.status_code == 200
    assert response.json() == ['Suite suite_not_exists does not exist']
