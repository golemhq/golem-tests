from projects.golem_api.pages import project
from projects.golem_api.pages import suite


def setup(data):
    project.using_project('general')
    data.suite_one = project.create_random_suite(data.project)
    data.suite_two = project.create_random_suite(data.project)


def test(data):
    response = suite.duplicate_suite(data.project, data.suite_one, data.suite_two)
    assert response.status_code == 200
    assert response.json() == ['A suite with that name already exists']
