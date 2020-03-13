from golem import actions

from projects.golem_api.pages import project
from projects.golem_api.pages import suite


def setup(data):
    project.using_project('general')
    data.suite = project.create_random_suite(data.project)


def test(data):
    new_suite_name = actions.random_str()
    response = suite.rename_suite(data.project, data.suite, new_suite_name)
    assert response.status_code == 200
    assert response.json()['errors'] == []
