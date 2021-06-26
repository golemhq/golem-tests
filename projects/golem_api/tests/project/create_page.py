from golem import actions

from projects.golem_api.pages import project
from projects.golem_api.pages import user_factory


def setup(data):
    project.using_project('general')


def test_create_page(data):
    page = actions.random_str()
    response = project.create_page(data.project, page)
    assert response.status_code == 200
    assert response.json()['errors'] == []
    assert project.page_exists(data.project, page)


def test_create_page_as_read_only_user(data):
    read_only = user_factory.create_user_if('general__read-only')
    response = project.create_page(data.project, actions.random_str(), user=read_only)
    assert response.status_code == 401


def test_create_page_already_exists(data):
    page_name = project.create_random_page(data.project)
    response = project.create_page(data.project, page_name)
    assert response.status_code == 200
    assert response.json()['errors'] == ['A page with that name already exists']
