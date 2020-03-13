from projects.golem_api.pages import project


def setup(data):
    data.project = project.create_random_project()


def test(data):
    response = project.save_environments(data.project, env_data={'env1': {}})
    assert response.status_code == 200
    assert response.json()['error'] == ''
    response = project.get_project_environments(data.project)
    assert response.json() == ['env1']
