from golem import actions

from projects.golem_api.pages import project
from projects.golem_api.pages import test_


def setup(data):
    project.using_project('general')
    actions.store('dir', actions.random_str())
    actions.store('test_name', actions.random_str())
    actions.store('test', '{}.{}'.format(data.dir, data.test_name))
    project.create_test_directory(data.project, data.dir)
    project.create_test(data.project, data.test)


def test(data):
    new_dir = actions.random_str()
    response = test_.rename_test_directory(data.project, data.dir, new_dir)
    assert response.status_code == 200
    assert response.json()['errors'] == []
    assert not project.get_test_exists(data.project, data.test).json()
    test_name = '{}.{}'.format(new_dir, data.test_name)
    assert project.get_test_exists(data.project, test_name).json()
