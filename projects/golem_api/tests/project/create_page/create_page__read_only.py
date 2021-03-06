from golem import actions

from projects.golem_api.pages import project
from projects.golem_api.pages import user_factory


def setup(data):
    project.using_project('general')
    actions.store('user', user_factory.create_user_if('general__read-only'))


def test(data):
    page = actions.random_str()
    response = project.create_page(data.project, page, user=data.user)
    assert response.status_code == 401
