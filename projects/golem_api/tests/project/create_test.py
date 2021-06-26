from golem import actions

from projects.golem_api.pages import project
from projects.golem_api.pages import user_factory


def setup(data):
    project.using_project('general')


def test_create_test_to_test_root_folder(data):
    test_name = actions.random_str()
    response = project.create_test(data.project, test_name)
    assert response.status_code == 200
    assert response.json()['errors'] == []
    assert project.test_exists(data.project, test_name)


def test_create_test_to_folder(data):
    test_name = '{}.{}'.format(actions.random_str(), actions.random_str())
    response = project.create_test(data.project, test_name)
    assert response.json()['errors'] == []
    assert project.test_exists(data.project, test_name)


def test_create_test_to_subfolder(data):
    test_name = '{}.{}.{}'.format(actions.random_str(), actions.random_str(), actions.random_str())
    response = project.create_test(data.project, test_name)
    assert response.json()['errors'] == []
    assert project.test_exists(data.project, test_name)


def test_create_test_existing_name(data):
    test_name = project.create_random_test(data.project)
    response = project.create_test(data.project, test_name)
    assert response.status_code == 200
    assert response.json()['errors'] == ['A test with that name already exists']


def test_create_test_as_read_only_user(data):
    read_only = user_factory.create_user_if('general__read-only')
    response = project.create_test(data.project, actions.random_str(), user=read_only)
    assert response.status_code == 401


def test_create_test_with_invalid_name(data):
    # invalid chars
    response = project.create_test(data.project, 'name-{}'.format(actions.random_str()))
    assert response.status_code == 200
    assert response.json()['errors'] == ['Only letters, numbers and underscores are allowed']
    # empty directory
    response = project.create_test(data.project, '.test_name')
    assert response.json()['errors'] == ['Directory name cannot be empty']
    # max length
    response = project.create_test(data.project, 'a'*151)
    assert response.json()['errors'] == ['Maximum name length is 150 characters']
    # empty name
    response = project.create_test(data.project, '')
    assert response.json()['errors'] == ['File name cannot be empty']
