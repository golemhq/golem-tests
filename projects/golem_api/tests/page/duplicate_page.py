from golem import actions

from projects.golem_api.pages import project
from projects.golem_api.pages import page
from projects.golem_api.pages import user_factory


def setup(data):
    project.using_project('general')
    data.page = project.create_random_page(data.project)


def test_duplicate_page(data):
    new_page_name = actions.random_str()
    response = page.duplicate_page(data.project, data.page, new_page_name)
    assert response.status_code == 200
    assert response.json() == []
    assert project.page_exists(data.project, new_page_name)


def test_duplicate_page_as_read_only_user(data):
    new_page_name = actions.random_str()
    read_only = user_factory.create_user_if('general__read-only')
    response = page.duplicate_page(data.project, data.page, new_page_name, user=read_only)
    assert response.status_code == 401


def test_duplicate_page_as_standard_user(data):
    new_page_name = actions.random_str()
    standard = user_factory.create_user_if('general__standard')
    response = page.duplicate_page(data.project, data.page, new_page_name, user=standard)
    assert response.status_code == 200
    assert response.json() == []
    assert project.page_exists(data.project, new_page_name)


def test_duplicate_page_does_not_exist(data):
    does_not_exist = actions.random_str()
    new_page_name = actions.random_str()
    response = page.duplicate_page(data.project, does_not_exist, new_page_name)
    assert response.status_code == 200
    assert response.json() == ['Page {} does not exist'.format(does_not_exist)]


def test_duplicate_page_destination_exists(data):
    new_page = project.create_random_page(data.project)
    response = page.duplicate_page(data.project, data.page, new_page)
    assert response.status_code == 200
    assert response.json() == ['A page with that name already exists']