from golem import actions

from projects.golem_api.pages import project


def setup(data):
    project.using_project('general')


def test(data):
    # to folder from root
    test_name = actions.random_str()
    full_name = '{}.{}'.format(actions.random_str(), test_name)
    response = project.create_test(data.project, full_name)
    assert response.status_code == 200
    assert response.json()['errors'] == []
    assert project.get_test_exists(data.project, full_name).json()
