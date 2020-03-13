from golem import actions

from projects.golem_api.pages import project
from projects.golem_api.pages import page


def setup(data):
    actions.store('project', 'general')
    actions.store('page_one', actions.random_str())
    actions.store('page_two', actions.random_str())
    project.create_project_if(data.project)
    project.create_page(data.project, data.page_one)
    project.create_page(data.project, data.page_two)


def test(data):
    response = page.duplicate_page(data.project, data.page_one, data.page_two)
    assert response.status_code == 200
    assert response.json() == ['A page with that name already exists']
