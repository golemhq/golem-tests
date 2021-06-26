from projects.golem_api.pages import project


def setup(data):
    data.project = project.create_random_project()


def test_get_projects(data):
    response = project.get_projects()
    assert response.status_code == 200
    assert data.project in response.json()
