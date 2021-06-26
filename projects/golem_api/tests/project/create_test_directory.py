from golem import actions

from projects.golem_api.pages import project


def setup(data):
    project.using_project('general')


def test_create_test_directory(data):
    response = project.create_test_directory(data.project, actions.random_str())
    assert response.status_code == 200
    assert response.json()['errors'] == []


def test_create_test_directory_exists(data):
    dir_one = actions.random_str()
    dir_two = '{}.{}'.format(actions.random_str(), actions.random_str())
    project.create_test_directory(data.project, dir_one)
    project.create_test_directory(data.project, dir_two)
    response = project.create_test_directory(data.project, dir_one)
    assert response.json()['errors'] == ['A directory with that name already exists']
    response = project.create_test_directory(data.project, dir_two)
    assert response.json()['errors'] == ['A directory with that name already exists']


def test_create_test_directory_with_invalid_name(data):
    dir_name = 'test-{}'.format(actions.random_str())
    response = project.create_test_directory(data.project, dir_name)
    assert response.json()['errors'] == ['Only letters, numbers and underscores are allowed']
