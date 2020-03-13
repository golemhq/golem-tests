from golem import actions

from projects.golem_api.pages import project
from projects.golem_api.pages import test_


def setup(data):
    project.using_project('general')


def test(data):
    test_name = actions.random_str()
    new_name = actions.random_str()
    response = test_.rename_test(data.project, test_name, new_name)
    assert response.json()['errors'] == ['Test {} does not exist'.format(test_name)]
