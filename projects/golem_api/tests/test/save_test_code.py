from projects.golem_api.pages import project
from projects.golem_api.pages import test_


def setup(data):
    project.using_project('general')
    data.test = project.create_random_test(data.project)


def test(data):
    response = test_.save_test_code(data.project, data.test, test_data='', content='')
    assert response.status_code == 200
    assert response.json()['error'] is None
