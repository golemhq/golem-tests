from projects.golem_api.pages import project
from projects.golem_api.pages import settings


def setup(data):
    data.project = project.create_random_project()


def test_get_project_settings(data):
    response = settings.get_project_settings(data.project)
    assert response.status_code == 200
