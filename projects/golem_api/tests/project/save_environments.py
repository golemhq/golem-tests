from projects.golem_api.pages import project
from projects.golem_api.pages import user_factory


def setup(data):
    data.project = project.create_random_project()


def test_save_environments(data):
    response = project.save_environments(data.project, env_data={'env1': {}})
    assert response.status_code == 200
    assert response.json()['error'] == ''
    response = project.get_project_environments(data.project)
    assert response.json() == ['env1']


def test_save_environments_as_standard_user(data):
    standard = user_factory.create_user_if('general__standard')
    response = project.save_environments(data.project, env_data={}, user=standard)
    assert response.status_code == 401
