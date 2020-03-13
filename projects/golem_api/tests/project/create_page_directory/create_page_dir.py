from golem import actions

from projects.golem_api.pages import project


def setup(data):
    project.using_project('general')


def test(data):
    dir_name = actions.random_str()
    response = project.create_page_directory(data.project, dir_name)
    assert response.status_code == 200
    assert response.json()['errors'] == []
