from golem import actions

from projects.golem_api.pages import project
from projects.golem_api.pages import suite


def setup(data):
    project.using_project('general')
    data.dir = actions.random_str()
    project.create_suite_directory(data.project, data.dir)


def test_delete_suite_directory(data):
    response = suite.delete_suite_directory(data.project, data.dir)
    assert response.status_code == 200
    assert response.json()['errors'] == []
