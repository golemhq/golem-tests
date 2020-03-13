from golem import actions

from projects.golem_api.pages import project


def setup(data):
    project.using_project('general')


def test(data):
    page = actions.random_str()
    response = project.create_page(data.project, page)
    assert response.status_code == 200
    assert response.json()['errors'] == []
    assert project.get_page_exists(data.project, page).json()
