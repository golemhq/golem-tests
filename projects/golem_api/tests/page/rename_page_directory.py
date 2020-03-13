from golem import actions

from projects.golem_api.pages import project
from projects.golem_api.pages import page


def setup(data):
    project.using_project('general')
    actions.store('dir', actions.random_str())
    project.create_page_directory(data.project, data.dir)
    data.page_name = actions.random_str()
    actions.store('page_full', '{}.{}'.format(data.dir, data.page_name))
    project.create_page(data.project, data.page_full)


def test(data):
    # rename page
    new_dir = actions.random_str()
    response = page.rename_page_directory(data.project, data.dir, new_dir)
    assert response.status_code == 200
    assert response.json()['errors'] == []
    # old page does not exist
    assert not project.get_page_exists(data.project, data.page_full).json()
    # new page exists
    page_full = '{}.{}'.format(new_dir, data.page_name)
    assert project.get_page_exists(data.project, page_full).json()
