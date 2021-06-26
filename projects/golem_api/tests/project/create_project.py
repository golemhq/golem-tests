from golem import actions

from projects.golem_api.pages import project
from projects.golem_api.pages import user_factory


def test_create_project(data):
    project_name = actions.random_str()
    response = project.create_project(project_name)
    assert response.status_code == 200
    assert response.json()['errors'] == []
    assert response.json()['project_name'] == project_name
    assert project.project_exists(project_name)


def test_create_project_as_admin_user(data):
    project_name = actions.random_str()
    user = user_factory.create_user_if('general__admin')
    response = project.create_project(project_name, user=user)
    assert response.status_code == 401


def test_create_project_already_exists(data):
    project_name = project.create_random_project()
    response = project.create_project(project_name)
    assert response.status_code == 200
    assert response.json()['errors'] == ['A project with that name already exists']


def test_create_project_name_is_too_short(data):
    response = project.create_project('no')
    assert response.status_code == 200
    assert response.json()['errors'] == ['Project name is too short']


def test_create_project_name_is_too_long(data):
    project_name = actions.random_str(51)
    response = project.create_project(project_name)
    assert response.status_code == 200
    assert response.json()['errors'] == ['Project name is too long']
