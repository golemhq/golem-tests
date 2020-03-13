from golem import actions

from projects.golem_api.pages import project
from projects.golem_api.pages import page


def setup(data):
    project.using_project('general')
    data.page = project.create_random_page(data.project)


def test(data):
    response = page.save_page_code(data.project, data.page, content='')
    assert response.status_code == 200
    assert response.json()['error'] is None
