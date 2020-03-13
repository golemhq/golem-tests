from golem import actions

from projects.golem_api.pages import project
from projects.golem_api.pages import test_


def setup(data):
    project.using_project('general')
    data.test_one = project.create_random_test(data.project)
    data.test_two = '{}.{}'.format(actions.random_str(), actions.random_str())
    project.create_test(data.project, data.test_two)


def test(data):
    response = test_.delete_test(data.project, data.test_one)
    assert response.status_code == 200
    assert response.json() == []
    assert not project.get_test_exists(data.project, data.test_one).json()
    test_.delete_test(data.project, data.test_two)
    assert not project.get_test_exists(data.project, data.test_two).json()
