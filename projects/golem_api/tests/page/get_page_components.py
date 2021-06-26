from projects.golem_api.pages import project
from projects.golem_api.pages import page
from projects.golem_api.pages import user_factory


def setup(data):
    project.using_project('general')
    data.page = project.create_random_page(data.project)


def test_get_page_components(data):
    response = page.get_page_components(data.project, data.page)
    assert response.status_code == 200
    assert response.json()['error'] == ''
    assert response.json()['components'] == {
        'code_lines': [''], 'elements': [], 'functions': [], 'import_lines': [], 'source_code': ''}


def test_get_page_components_does_not_exist(data):
    page_name = 'this_page_does_not_exist'
    response = page.get_page_components(data.project, page_name)
    assert response.status_code == 200
    assert response.json()['error'] == 'page does not exist'


def test_get_page_components_as_read_only(data):
    read_only = user_factory.create_user_if('general__read-only')
    response = page.get_page_components(data.project, data.page, user=read_only)
    assert response.status_code == 200
    assert response.json()['error'] == ''


def test_get_page_components_as_reports_only(data):
    reports_only = user_factory.create_user_if('general__reports-only')
    response = page.get_page_components(data.project, data.page, user=reports_only)
    assert response.status_code == 401
