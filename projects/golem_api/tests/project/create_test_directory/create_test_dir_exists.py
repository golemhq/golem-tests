from golem import actions

from projects.golem_api.pages import project


def setup(data):
    project.using_project('general')
    actions.store('dir_one', actions.random_str())
    actions.store('dir_two', '{}.{}'.format(actions.random_str(), actions.random_str()))
    project.create_test_directory(data.project, data.dir_one)
    project.create_test_directory(data.project, data.dir_two)


def test(data):
    response = project.create_test_directory(data.project, data.dir_one)
    assert response.json()['errors'] == ['A directory with that name already exists']
    response = project.create_test_directory(data.project, data.dir_two)
    assert response.json()['errors'] == ['A directory with that name already exists']
