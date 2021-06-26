from golem import actions

from projects.golem_api.pages import project


def setup(data):
    project.using_project('general')


def test_project_test_exists(data):
    test_name = actions.random_str()
    assert project.get_test_exists(data.project, test_name).json() is False
    project.create_test(data.project, test_name)
    assert project.get_test_exists(data.project, test_name).json() is True
