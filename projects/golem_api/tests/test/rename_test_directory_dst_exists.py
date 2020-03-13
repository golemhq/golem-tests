from golem import actions

from projects.golem_api.pages import project
from projects.golem_api.pages import test_


def setup(data):
    project.using_project('general')
    actions.store('dir_one', actions.random_str())
    actions.store('dir_two', actions.random_str())
    project.create_test_directory(data.project, data.dir_one)
    project.create_test_directory(data.project, data.dir_two)


def test(data):
    response = test_.rename_test_directory(data.project, data.dir_one, data.dir_two)
    assert response.json()['errors'] == ['Path {} already exists'.format(data.dir_two)]
    # to same name
    response = test_.rename_test_directory(data.project, data.dir_one, data.dir_one)
    assert response.json()['errors'] == ['Path {} already exists'.format(data.dir_one)]
