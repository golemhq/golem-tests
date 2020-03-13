from projects.golem_api.pages import project


def test(data):
    project_name = project.create_random_project()
    response = project.create_project(project_name)
    assert response.status_code == 200
    assert 'A project with that name already exists' in response.json()['errors']
