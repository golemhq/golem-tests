from golem import actions

from projects.golem_api.pages import project
from projects.golem_api.pages import suite


def setup(data):
    project.using_project('general')
    actions.store('dir', actions.random_str())
    project.create_suite_directory(data.project, data.dir)


def test(data):
    actions.store('new_dir', actions.random_str())
    response = suite.rename_suite_directory(data.project, data.dir, data.new_dir)
    assert response.status_code == 200
    assert response.json()['errors'] == []
