from golem import actions

from projects.golem_api.pages import project


def setup(data):
    project.using_project('general')


def test(data):
    page = actions.random_str()
    response = project.get_page_exists(data.project, page)
    assert response.json() is False
    project.create_page(data.project, page)
    response = project.get_page_exists(data.project, page)
    assert response.json() is True
