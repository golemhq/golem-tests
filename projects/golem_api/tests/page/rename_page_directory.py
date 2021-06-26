from golem import actions

from projects.golem_api.pages import project
from projects.golem_api.pages import page


def setup(data):
    project.using_project('general')
    data.dir = actions.random_str()
    data.page_name = actions.random_str()
    data.page_full = '{}.{}'.format(data.dir, data.page_name)
    project.create_page_directory(data.project, data.dir)
    project.create_page(data.project, data.page_full)


def test_rename_page_directory(data):
    # rename page
    new_dir = actions.random_str()
    response = page.rename_page_directory(data.project, data.dir, new_dir)
    assert response.status_code == 200
    assert response.json()['errors'] == []
    # old page does not exist anymore
    assert not project.page_exists(data.project, data.page_full)
    # new page exists
    new_page_full = '{}.{}'.format(new_dir, data.page_name)
    assert project.page_exists(data.project, new_page_full)
