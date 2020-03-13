from golem import actions

from projects.golem_api.pages import project
from projects.golem_api.pages import test_


def setup(data):
    project.using_project('general')
    data.test = project.create_random_test(data.project)


def test(data):
    new_name = actions.random_str()
    response = test_.duplicate_test(data.project, data.test, new_name)
    assert response.status_code == 200
    assert response.json() == []
    # duplicate to another folder
    new_name_two = '{}.{}'.format(actions.random_str(), actions.random_str())
    test_.duplicate_test(data.project, data.test, new_name_two)
    assert project.get_test_exists(data.project, data.test).json()
    assert project.get_test_exists(data.project, new_name).json()
    assert project.get_test_exists(data.project, new_name_two).json()
