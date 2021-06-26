from golem import actions

from projects.golem_api.pages import project
from projects.golem_api.pages import suite


def setup(data):
    project.using_project('general')


def test_run_suite(data):
    suite_name = project.create_random_suite(data.project)
    response = suite.run_suite(data.project, suite_name)
    assert response.status_code == 200
    assert type(response.json()) == str  # timestamp


def test_run_suite_doesnt_exist(data):
    response = suite.run_suite(data.project, actions.random_str())
    assert response.status_code == 200
    assert type(response.json()) == str  # currently does not return an error
