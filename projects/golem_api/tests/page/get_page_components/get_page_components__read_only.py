from golem import actions

from projects.golem_api.pages import project
from projects.golem_api.pages import page
from projects.golem_api.pages import user_factory


def setup(data):
    project.using_project('general')
    data.page = project.create_random_page(data.project)
    actions.store('user', user_factory.create_user_if('general__read-only'))


def test(data):
    response = page.get_page_components(data.project, data.page)
    assert response.status_code == 200
    assert response.json()['error'] == ''
    assert response.json()['contents'] == []
