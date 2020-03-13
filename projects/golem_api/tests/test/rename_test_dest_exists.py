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
    response = test_.rename_test(data.project, data.test_one, data.test_one)
    assert response.json()['errors'] == ['A file with that name already exists']
    # rename test in folder
    response = test_.rename_test(data.project, data.test_two, data.test_two)
    assert response.json()['errors'] == ['A file with that name already exists']
