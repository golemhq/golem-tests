from projects.golem_api.pages import project
from projects.golem_api.pages import test_


def setup(data):
    project.using_project('general')
    data.test_one = project.create_random_test(data.project)
    data.test_two = project.create_random_test(data.project)


def test(data):
    response = test_.duplicate_test(data.project, data.test_one, data.test_two)
    assert response.status_code == 200
    assert response.json() == ['A test with that name already exists']
    # duplicate with same name
    response = test_.duplicate_test(data.project, data.test_one, data.test_one)
    assert response.json() == ['New test name cannot be the same as the original']
