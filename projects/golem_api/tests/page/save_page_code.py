from golem import actions

from projects.golem_api.pages import project
from projects.golem_api.pages import page
from projects.golem_api.pages import user_factory


def setup(data):
    project.using_project('general')
    data.page = project.create_random_page(data.project)


def test_save_page_code(data):
    response = page.save_page_code(data.project, data.page, content='test = 2')
    assert response.status_code == 200
    assert response.json()['error'] is None
    response = page.get_page_components(data.project, data.page)
    assert response.json()['components']['source_code'] == 'test = 2'


def test_save_page_code_with_read_only_user(data):
    read_only = user_factory.create_user_if('general__read-only')
    response = page.save_page_code(data.project, data.page, content='', user=read_only)
    assert response.status_code == 401


def test_save_page_code_with_standard_user(data):
    standard_user = user_factory.create_user_if('general__standard')
    response = page.save_page_code(data.project, data.page, content='', user=standard_user)
    assert response.status_code == 200
    assert response.json()['error'] is None
