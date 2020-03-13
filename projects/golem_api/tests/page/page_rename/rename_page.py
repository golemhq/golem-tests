from golem import actions

from projects.golem_api.pages import project
from projects.golem_api.pages import page


def setup(data):
    project.using_project('general')
    data.page = project.create_random_page(data.project)


def test(data):
    new_page_name = actions.random_str()
    response = page.rename_page(data.project, data.page, new_page_name)
    assert response.status_code == 200
    assert response.json()['errors'] == []
    assert not project.get_page_exists(data.project, data.page).json()
    assert project.get_page_exists(data.project, new_page_name).json()
