from projects.golem_api.pages import project
from projects.golem_api.pages import page


def setup(data):
    project.using_project('general')
    data.page = project.create_random_page(data.project)


def test(data):
    response = page.get_page_components(data.project, data.page)
    assert response.status_code == 200
    assert response.json()['error'] == ''
    assert response.json()['contents'] == []
