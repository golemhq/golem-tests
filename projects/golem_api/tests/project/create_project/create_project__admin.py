from golem import actions

from projects.golem_api.pages import project
from projects.golem_api.pages import user_factory


def test(data):
    project_name = actions.random_str()
    user = user_factory.create_user_if('general__admin')
    response = project.create_project(project_name, user=user)
    assert response.status_code == 401
