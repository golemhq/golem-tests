from golem import actions

from projects.golem_api.pages import project
from projects.golem_api.pages import page


def setup(data):
    project.using_project('general')
    data.page = project.create_random_page(data.project)


def test(data):
    response = page.save_page(data.project, data.page, elements=[], functions=[],
                              import_lines=[])
    assert response.status_code == 200
    assert response.json() == 'page-saved'
