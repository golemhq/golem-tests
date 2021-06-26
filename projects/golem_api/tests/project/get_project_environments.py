from projects.golem_api.pages import project
from projects.golem_api.pages import user_factory


def test_get_project_environments(data):
    data.project = project.create_random_project()
    response = project.get_project_environments(data.project)
    assert response.status_code == 200
    assert response.json() == []


def test_get_project_environments_as_reports_only(data):
    read_only = user_factory.create_user_if('general__reports-only')
    response = project.get_project_environments(data.project, user=read_only)
    assert response.status_code == 401
