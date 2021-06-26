from golem import actions

from projects.golem_api.pages import project
from projects.golem_api.pages import user_factory


def setup(data):
    project.using_project('general')


def test_create_suite(data):
    response = project.create_suite(data.project, actions.random_str())
    assert response.status_code == 200
    assert response.json()['errors'] == []


def test_create_suite_as_standard_user(data):
    standard = user_factory.create_user_if('general__standard')
    suite = actions.random_str()
    response = project.create_suite(data.project, suite, user=standard)
    assert response.status_code == 200


def test_create_suite_as_read_only_user(data):
    read_only = user_factory.create_user_if('general__read-only')
    suite = actions.random_str()
    response = project.create_suite(data.project, suite, user=read_only)
    assert response.status_code == 401


def test_create_suite_exists(data):
    suite_name = project.create_random_suite(data.project)
    response = project.create_suite(data.project, suite_name)
    assert response.status_code == 200
    assert response.json()['errors'] == ['A suite with that name already exists']
