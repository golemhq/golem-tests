from golem import actions

from projects.golem_api.pages import project


def test(data):
    project_name = actions.random_str()
    project.create_project(project_name)
    assert project.get_project_exists(project_name).json() is True
    response = project.delete_project(project_name)
    assert response.json()['errors'] == []
    assert project.get_project_exists(project_name).json() is False
