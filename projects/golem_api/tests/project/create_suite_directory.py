from golem import actions

from projects.golem_api.pages import project


def setup(data):
    project.using_project('general')


def test_create_suite_directory(data):
    response = project.create_suite_directory(data.project, actions.random_str())
    assert response.status_code == 200
    assert response.json()['errors'] == []


def test_create_suite_directory_exists(data):
    dir_name = actions.random_str()
    project.create_suite_directory(data.project, dir_name)
    response = project.create_suite_directory(data.project, dir_name)
    assert response.json()['errors'] == ['A directory with that name already exists']
