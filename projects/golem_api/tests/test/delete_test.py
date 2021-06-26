from golem import actions

from projects.golem_api.pages import project
from projects.golem_api.pages import test_


def setup(data):
    project.using_project('general')


def test_delete_test(data):
    test_one = project.create_random_test(data.project)
    response = test_.delete_test(data.project, test_one)
    assert response.status_code == 200
    assert response.json() == []
    assert not project.test_exists(data.project, test_one)

    test_two = '{}.{}'.format(actions.random_str(), actions.random_str())
    project.create_test(data.project, test_two)
    test_.delete_test(data.project, test_two)
    assert not project.test_exists(data.project, test_two)


def test_delete_test_doesnt_exist(data):
    test_name = actions.random_str()
    response = test_.delete_test(data.project, test_name)
    assert response.status_code == 200
    assert response.json() == ['Test {} does not exist'.format(test_name)]
