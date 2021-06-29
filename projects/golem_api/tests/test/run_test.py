from projects.golem_api.pages import project
from projects.golem_api.pages import test_


def setup(data):
    project.using_project('general')
    data.test = project.create_test(data.project)


def test_run_test(data):
    response = test_.run_test(data.project, data.test)
    assert response.status_code == 200
    assert type(response.json()) == str
