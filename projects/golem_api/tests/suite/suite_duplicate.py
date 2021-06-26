from golem import actions

from projects.golem_api.pages import project
from projects.golem_api.pages import suite


def setup(data):
    project.using_project('general')
    data.suite = project.create_random_suite(data.project)


def test_duplicate_suite(data):
    new_suite_name = actions.random_str()
    response = suite.duplicate_suite(data.project, data.suite, new_suite_name)
    assert response.status_code == 200
    assert response.json() == []
    assert project.suite_exists(data.project, data.suite)
    assert project.suite_exists(data.project, new_suite_name)


def test_duplicate_suite_destination_exists(data):
    suite_one = project.create_random_suite(data.project)
    response = suite.duplicate_suite(data.project, suite_one, data.suite)
    assert response.status_code == 200
    assert response.json() == ['A suite with that name already exists']
