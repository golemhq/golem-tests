from golem import actions

from projects.golem_api.pages import project


def test(data):
    project_name = actions.random_str()
    response = project.delete_project(project_name)
    assert response.json()['errors'] == ['Project {} does not exist'.format(project_name)]
