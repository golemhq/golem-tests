from golem import actions

from projects.golem_api.pages import project
from projects.golem_api.pages import test_


def setup(data):
    project.using_project('general')


def test_rename_test(data):
    test_one = project.create_random_test(data.project)
    new_test_name = actions.random_str()
    response = test_.rename_test(data.project, test_one, new_test_name)
    assert response.status_code == 200
    assert response.json()['errors'] == []
    assert not project.test_exists(data.project, test_one)
    assert project.test_exists(data.project, new_test_name)


def test_rename_test_in_folder(data):
    test_two = '{}.{}'.format(actions.random_str(), actions.random_str())
    project.create_test(data.project, test_two)
    new_test_name_two = '{}.{}'.format(actions.random_str(), actions.random_str())
    response = test_.rename_test(data.project, test_two, new_test_name_two)
    assert response.json()['errors'] == []
    assert not project.test_exists(data.project, test_two)
    assert project.test_exists(data.project, new_test_name_two)


def test_rename_test_destination_exists(data):
    test_one = project.create_random_test(data.project)
    response = test_.rename_test(data.project, test_one, test_one)
    assert response.json()['errors'] == ['A file with that name already exists']


def test_rename_test_with_invalid_name(data):
    test_name = project.create_random_test(data.project)
    new_name = 'test-{}'.format(actions.random_str())
    response = test_.rename_test(data.project, test_name, new_name)
    assert response.status_code == 200
    assert response.json()['errors'] == ['Only letters, numbers and underscores are allowed']
    assert project.test_exists(data.project, test_name)
    assert not project.test_exists(data.project, new_name)


def test_rename_test_does_not_exist(data):
    test_name = actions.random_str()
    new_name = actions.random_str()
    response = test_.rename_test(data.project, test_name, new_name)
    assert response.json()['errors'] == ['Test {} does not exist'.format(test_name)]
