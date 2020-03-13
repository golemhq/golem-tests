from golem import actions

from projects.golem_api.pages import project
from projects.golem_api.pages import page


def setup(data):
    project.using_project('general')
    data.page = project.create_random_page(data.project)


def test(data):
    new_name = 'invalid-{}'.format(actions.random_str())
    response = page.duplicate_page(data.project, data.page, new_name)
    assert response.json() == ['Only letters, numbers and underscores are allowed']
    assert project.get_page_exists(data.project, data.page).json()
    assert not project.get_page_exists(data.project, new_name).json()
