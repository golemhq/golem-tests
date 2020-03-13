from golem import actions

from projects.golem_api.pages import project
from projects.golem_api.pages import test_


def setup(data):
    project.using_project('general')
    data.test = project.create_random_test(data.project)


def test(data):
    new_name = 'test-{}'.format(actions.random_str())
    response = test_.duplicate_test(data.project, data.test, new_name)
    assert response.status_code == 200
    assert response.json() == ['Only letters, numbers and underscores are allowed']
    assert project.get_test_exists(data.project, data.test).json()
    assert not project.get_test_exists(data.project, new_name).json()
