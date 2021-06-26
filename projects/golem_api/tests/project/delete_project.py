from golem import actions

from projects.golem_api.pages import project
from projects.golem_api.pages import user_factory


def test_delete_project(data):
    project_name = project.create_random_project()
    assert project.project_exists(project_name)
    response = project.delete_project(project_name)
    assert response.json()['errors'] == []
    assert not project.project_exists(project_name)


def test_delete_project_does_not_exist(data):
    project_name = actions.random_str()
    response = project.delete_project(project_name)
    assert response.json()['errors'] == ['Project {} does not exist'.format(project_name)]


def test_delete_project_as_admin_user(data):
    project_name = project.create_random_project()
    admin_user = user_factory.create_user_if('{}__admin'.format(project_name))
    response = project.delete_project(project_name, user=admin_user)
    assert response.status_code == 401
