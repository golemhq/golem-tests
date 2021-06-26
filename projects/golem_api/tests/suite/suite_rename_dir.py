from golem import actions

from projects.golem_api.pages import project
from projects.golem_api.pages import suite


def setup(data):
    project.using_project('general')
    data.dir = actions.random_str()
    project.create_suite_directory(data.project, data.dir)


def test_rename_suite_directory(data):
    new_dir = actions.random_str()
    response = suite.rename_suite_directory(data.project, data.dir, new_dir)
    assert response.status_code == 200
    assert response.json()['errors'] == []
