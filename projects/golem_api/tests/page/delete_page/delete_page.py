from projects.golem_api.pages import project
from projects.golem_api.pages import page


def setup(data):
    project.using_project('general')
    data.page = project.create_random_page(data.project)


def test(data):
    response = page.delete_page(data.project, data.page)
    assert response.status_code == 200
    assert response.json() == []
    assert not project.get_page_exists(data.project, data.page).json()
