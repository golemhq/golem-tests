from projects.golem_api.pages import project
from projects.golem_api.pages import page
from projects.golem_api.pages import user_factory


def setup(data):
    project.using_project('general')


def test_delete_page(data):
    page_name = project.create_random_page(data.project)
    response = page.delete_page(data.project, page_name)
    assert response.status_code == 200
    assert response.json() == []
    assert not project.page_exists(data.project, page_name)


def test_delete_page_as_admin_user(data):
    admin = user_factory.create_user_if('general__admin')
    page_name = project.create_random_page(data.project)
    response = page.delete_page(data.project, page_name, user=admin)
    assert response.status_code == 200


def test_delete_page_as_standard_user(data):
    standard = user_factory.create_user_if('general__standard')
    page_name = project.create_random_page(data.project)
    response = page.delete_page(data.project, page_name, user=standard)
    assert response.status_code == 401


def test_delete_page_does_not_exist(data):
    response = page.delete_page(data.project, 'page_not_exists')
    assert response.status_code == 200
    assert response.json() == ['Page page_not_exists does not exist']
