from projects.golem_api.pages import project
from projects.golem_api.pages import test_


def setup(data):
    project.using_project('general')


def test(data):
    response = test_.delete_test(data.project, 'test_not_exist')
    assert response.status_code == 200
    assert response.json() == ['Test test_not_exist does not exist']
