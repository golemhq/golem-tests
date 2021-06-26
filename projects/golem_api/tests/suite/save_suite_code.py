from projects.golem_api.pages import project
from projects.golem_api.pages import suite


def setup(data):
    project.using_project('general')
    data.suite = project.create_random_suite(data.project)


def test_save_suite_code(data):
    response = suite.save_suite_code(data.project, data.suite, 'tests = []')
    assert response.status_code == 200
    assert response.json()['error'] is None
