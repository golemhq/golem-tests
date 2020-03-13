from golem import actions

from projects.golem_api.pages import project


def setup(data):
    project.using_project('general')


def test(data):
    suite = actions.random_str()
    response = project.get_suite_exists(data.project, suite)
    assert response.json() is False
    project.create_suite(data.project, suite)
    response = project.get_suite_exists(data.project, suite)
    assert response.json() is True
