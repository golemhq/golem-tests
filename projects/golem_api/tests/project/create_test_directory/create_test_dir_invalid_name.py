from golem import actions

from projects.golem_api.pages import project


def setup(data):
    project.using_project('general')


def test(data):
    dir_name = 'test-{}'.format(actions.random_str())
    response = project.create_test_directory(data.project, dir_name)
    assert response.json()['errors'] == ['Only letters, numbers and underscores are allowed']
