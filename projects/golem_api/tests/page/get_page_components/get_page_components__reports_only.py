from golem import actions

from projects.golem_api.pages import project
from projects.golem_api.pages import page
from projects.golem_api.pages import user_factory


def setup(data):
    project.using_project('general')
    actions.store('user', user_factory.create_user_if('general__reports-only'))
    data.page = project.create_random_page(data.project)


def test(data):
    response = page.get_page_components(data.project, data.page, user=data.user)
    assert response.status_code == 401
