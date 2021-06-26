from golem import actions

from projects.golem_api.pages import project
from projects.golem_api.pages import test_


def setup(data):
    project.using_project('general')


def test_delete_test_directory(data):
    dirname = actions.random_str()
    project.create_test_directory(data.project, dirname)
    response = test_.delete_test_directory(data.project, dirname)
    assert response.status_code == 200
    assert response.json()['errors'] == []


def test_delete_test_directory_with_a_test_inside(data):
    dir_two = actions.random_str()
    test = '{}.{}'.format(dir_two, actions.random_str())
    project.create_test(data.project, test)
    test_.delete_test_directory(data.project, dir_two)
    assert not project.test_exists(data.project, test)
