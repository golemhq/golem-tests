from golem import actions

from projects.golem_api.pages import project
from projects.golem_api.pages import page


def setup(data):
    project.using_project('general')
    actions.store('dir', actions.random_str())
    project.create_page_directory(data.project, data.dir)


def test(data):
    response = page.delete_page_directory(data.project, data.dir)
    assert response.status_code == 200
    assert response.json()['errors'] == []
