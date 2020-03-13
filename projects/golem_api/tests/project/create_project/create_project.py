from golem import actions

from projects.golem_api.pages import project


def test(data):
    project_name = actions.random_str()
    response = project.create_project(project_name)
    assert response.status_code == 200
    assert response.json()['errors'] == []
    assert response.json()['project_name'] == project_name
    response = project.get_project_exists(project_name)
    assert response.json() is True
