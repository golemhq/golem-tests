from golem import actions

from projects.golem_api.pages import project
from projects.golem_api.pages import test_


def setup(data):
    project.using_project('general')
    actions.store('dir', actions.random_str())
    project.create_test_directory(data.project, data.dir)
    actions.store('dir_two', actions.random_str())
    actions.store('test', '{}.{}'.format(data.dir_two, actions.random_str()))
    project.create_test(data.project, data.test)


def test(data):
    response = test_.delete_test_directory(data.project, data.dir)
    assert response.status_code == 200
    assert response.json()['errors'] == []
    # delete a folder with a test inside
    test_.delete_test_directory(data.project, data.dir_two)
    assert not project.get_test_exists(data.project, data.test).json()
