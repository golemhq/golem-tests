from golem import actions

from projects.golem_api.pages import project
from projects.golem_api.pages import test_


def setup(data):
    project.using_project('general')
    data.test_one = project.create_random_test(data.project)
    data.test_two = '{}.{}'.format(actions.random_str(), actions.random_str())
    project.create_test(data.project, data.test_two)


def test(data):
    # rename test in root
    new_test_name = actions.random_str()
    response = test_.rename_test(data.project, data.test_one, new_test_name)
    assert response.status_code == 200
    assert response.json()['errors'] == []
    assert not project.get_test_exists(data.project, data.test_one).json()
    assert project.get_test_exists(data.project, new_test_name).json()
    # rename test in folder
    new_test_name_two = '{}.{}'.format(actions.random_str(), actions.random_str())
    response = test_.rename_test(data.project, data.test_two, new_test_name_two)
    assert response.json()['errors'] == []
    assert not project.get_test_exists(data.project, data.test_two).json()
    assert project.get_test_exists(data.project, new_test_name_two).json()