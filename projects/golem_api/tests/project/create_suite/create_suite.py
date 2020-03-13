from golem import actions

from projects.golem_api.pages import project


def setup(data):
    project.using_project('general')


def test(data):
    suite = actions.random_str()
    response = project.create_suite(data.project, suite)
    assert response.status_code == 200
    assert response.json()['errors'] == []
