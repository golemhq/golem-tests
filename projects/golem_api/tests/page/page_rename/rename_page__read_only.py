from golem import actions

from projects.golem_api.pages import project
from projects.golem_api.pages import page
from projects.golem_api.pages import user_factory


def setup(data):
    project.using_project('general')
    data.page = project.create_random_page(data.project)
    actions.store('user', user_factory.create_user_if('general__read-only'))


def test(data):
    new_page_name = actions.random_str()
    response = page.rename_page(data.project, data.page, new_page_name, user=data.user)
    assert response.status_code == 401
