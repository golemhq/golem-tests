from golem import actions

from projects.golem_api.pages import project
from projects.golem_api.pages import user_factory


def setup(data):
    project.using_project('general')
    actions.store('user', user_factory.create_user_if('general__reports-only'))


def test(data):
    response = project.get_project_environments(data.project, user=data.user)
    assert response.status_code == 401
