from projects.golem_api.pages import project
from projects.golem_api.pages import suite


def setup(data):
    project.using_project('general')
    data.suite = project.create_random_suite(data.project)


def test(data):
    response = suite.run_suite(data.project, data.suite)
    assert response.status_code == 200
    assert type(response.json()) == str
