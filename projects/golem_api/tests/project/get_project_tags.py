from projects.golem_api.pages import project
from projects.golem_api.pages import test_


def setup(data):
    data.project = project.create_random_project()


def test_get_project_tags(data):
    response = project.get_project_tags(data.project)
    assert response.status_code == 200
    assert response.json() == []
    # add a test with one tag
    test_name = project.create_random_test(data.project)
    test_.save_test(data.project, test_name, tags=['tag1'])
    response = project.get_project_tags(data.project)
    assert response.status_code == 200
    assert response.json() == ['tag1']
