from golem import actions

from projects.golem_api.pages import project
from projects.golem_api.pages import test_


def setup(data):
    project.using_project('general')
    data.test = project.create_test(data.project)


def test_duplicate_test(data):
    new_name = actions.random_str()
    response = test_.duplicate_test(data.project, data.test, new_name)
    assert response.status_code == 200
    assert response.json() == []
    assert project.test_exists(data.project, new_name)
    assert project.test_exists(data.project, data.test)


def test_duplicate_test_to_another_folder(data):
    new_name_two = '{}.{}'.format(actions.random_str(), actions.random_str())
    test_.duplicate_test(data.project, data.test, new_name_two)
    assert project.test_exists(data.project, new_name_two)


def test_duplicate_test_destination_exists(data):
    test_name = project.create_test(data.project)
    response = test_.duplicate_test(data.project, data.test, test_name)
    assert response.status_code == 200
    assert response.json() == ['A test with that name already exists']


def test_duplicate_test_with_same_name(data):
    response = test_.duplicate_test(data.project, data.test, data.test)
    assert response.json() == ['New test name cannot be the same as the original']


def test_duplicate_name_with_invalid_name(data):
    new_name = 'test-{}'.format(actions.random_str())
    response = test_.duplicate_test(data.project, data.test, new_name)
    assert response.status_code == 200
    assert response.json() == ['Only letters, numbers and underscores are allowed']
    assert project.test_exists(data.project, data.test)
    assert not project.test_exists(data.project, new_name)
