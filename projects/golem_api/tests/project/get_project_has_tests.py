from golem import actions

from projects.golem_api.pages import project


def setup(data):
    data.project = project.create_random_project()


def test(data):
    response = project.get_project_has_tests(data.project)
    assert not response.json()
    project.create_test(data.project, actions.random_str())
    response = project.get_project_has_tests(data.project)
    assert response.json()
