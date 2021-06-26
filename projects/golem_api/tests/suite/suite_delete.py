from projects.golem_api.pages import project
from projects.golem_api.pages import suite


def setup(data):
    project.using_project('general')
    data.suite = project.create_random_suite(data.project)


def test_delete_suite(data):
    response = suite.delete_suite(data.project, data.suite)
    assert response.status_code == 200
    assert response.json() == []
    assert not project.suite_exists(data.project, data.suite)


def test_delete_suite_doesnt_exist(data):
    response = suite.delete_suite(data.project, 'suite_not_exists')
    assert response.status_code == 200
    assert response.json() == ['Suite suite_not_exists does not exist']
