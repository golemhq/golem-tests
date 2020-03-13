from golem import actions

from projects.golem_api.pages import project


def setup(data):
    project.using_project('general')


def test(data):
    # to root
    test_one = actions.random_str()
    response = project.create_test(data.project, test_one)
    assert response.status_code == 200
    assert response.json()['errors'] == []
    # to folder
    test_two = '{}.{}'.format(actions.random_str(), actions.random_str())
    response = project.create_test(data.project, test_two)
    assert response.json()['errors'] == []
    # to sub folder
    test_three = '{}.{}.{}'.format(actions.random_str(), actions.random_str(), actions.random_str())
    response = project.create_test(data.project, test_three)
    assert response.json()['errors'] == []
