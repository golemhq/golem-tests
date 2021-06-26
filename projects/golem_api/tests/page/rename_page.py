from golem import actions

from projects.golem_api.pages import project
from projects.golem_api.pages import page
from projects.golem_api.pages import user_factory


def setup(data):
    project.using_project('general')


def test_rename_page(data):
    page_name = project.create_random_page(data.project)
    new_page_name = actions.random_str()
    response = page.rename_page(data.project, page_name, new_page_name)
    assert response.status_code == 200
    assert response.json()['errors'] == []
    assert not project.page_exists(data.project, page_name)
    assert project.page_exists(data.project, new_page_name)


def test_rename_page_does_not_exist(data):
    page_name = actions.random_str()
    new_page_name = actions.random_str()
    response = page.rename_page(data.project, page_name, new_page_name)
    assert response.status_code == 200
    assert response.json()['errors'] == ['Page {} does not exist'.format(page_name)]
    assert not project.page_exists(data.project, new_page_name)


def test_rename_page_as_standard_user(data):
    page_name = project.create_random_page(data.project)
    new_page_name = actions.random_str()
    standard = user_factory.create_user_if('general__standard')
    response = page.rename_page(data.project, page_name, new_page_name, user=standard)
    assert response.status_code == 200
    assert project.page_exists(data.project, new_page_name)


def test_rename_page_as_read_only_user(data):
    page_name = project.create_random_page(data.project)
    read_only = user_factory.create_user_if('general__read-only')
    new_page_name = actions.random_str()
    response = page.rename_page(data.project, page_name, new_page_name, user=read_only)
    assert response.status_code == 401
