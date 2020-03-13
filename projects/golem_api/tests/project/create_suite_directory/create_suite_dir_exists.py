from golem import actions

from projects.golem_api.pages import project


def setup(data):
    project.using_project('general')
    actions.store('dir_name', actions.random_str())
    project.create_suite_directory(data.project, data.dir_name)


def test(data):
    response = project.create_suite_directory(data.project, data.dir_name)
    assert response.json()['errors'] == ['A directory with that name already exists']
