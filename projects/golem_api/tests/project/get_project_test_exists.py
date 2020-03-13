from golem import actions

from projects.golem_api.pages import project


def setup(data):
    project.using_project('general')


def test(data):
    test_name = actions.random_str()
    response = project.get_test_exists(data.project, test_name)
    assert response.json() is False
    project.create_test(data.project, test_name)
    response = project.get_test_exists(data.project, test_name)
    assert response.json() is True
