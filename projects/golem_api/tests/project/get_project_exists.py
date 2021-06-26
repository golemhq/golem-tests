from golem import actions

from projects.golem_api.pages import project


def setup(data):
    project.using_project('general')


def test_project_exists(data):
    response = project.get_project_exists(data.project)
    assert response.json() is True


def test_project_does_not_exist(data):
    response = project.get_project_exists(actions.random_str())
    assert response.json() is False
