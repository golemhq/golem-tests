from golem import actions

from projects.golem_api.pages import project
from projects.golem_api.pages import test_


def setup(data):
    project.using_project('general')


def test_rename_test_directory(data):
    # rename a test directory with a test inside
    dirname = actions.random_str()
    test_name = actions.random_str()
    test_path = '{}.{}'.format(dirname, test_name)
    project.create_test_directory(data.project, dirname)
    project.create_test(data.project, test_path)

    new_dir = actions.random_str()
    response = test_.rename_test_directory(data.project, dirname, new_dir)
    assert response.status_code == 200
    assert response.json()['errors'] == []
    assert not project.test_exists(data.project, test_path)
    new_test_path = '{}.{}'.format(new_dir, test_name)
    assert project.test_exists(data.project, new_test_path)


def test_rename_test_directory_destination_exists(data):
    dir_one = actions.random_str()
    dir_two = actions.random_str()
    project.create_test_directory(data.project, dir_one)
    project.create_test_directory(data.project, dir_two)
    response = test_.rename_test_directory(data.project, dir_one, dir_two)
    assert response.json()['errors'] == ['Path {} already exists'.format(dir_two)]


def test_rename_test_directory_to_same_name(data):
    dir_one = actions.random_str()
    project.create_test_directory(data.project, dir_one)
    response = test_.rename_test_directory(data.project, dir_one, dir_one)
    assert response.json()['errors'] == ['Path {} already exists'.format(dir_one)]


def test_rename_test_directory_to_parent(data):
    dirname = actions.random_str()
    subdir = '{}.{}'.format(dirname, actions.random_str())
    project.create_test_directory(data.project, dirname)
    project.create_test_directory(data.project, subdir)

    response = test_.rename_test_directory(data.project, subdir, dirname)
    assert response.json()['errors'] == ['Path {} already exists'.format(dirname)]
