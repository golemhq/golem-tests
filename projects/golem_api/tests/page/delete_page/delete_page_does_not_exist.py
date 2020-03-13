from projects.golem_api.pages import project
from projects.golem_api.pages import page


def setup(data):
    project.using_project('general')


def test(data):
    response = page.delete_page(data.project, 'page_not_exists')
    assert response.status_code == 200
    assert response.json() == ['Page page_not_exists does not exist']
