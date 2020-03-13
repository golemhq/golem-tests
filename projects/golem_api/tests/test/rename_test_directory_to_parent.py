from golem import actions

from projects.golem_api.pages import project
from projects.golem_api.pages import test_


def setup(data):
    project.using_project('general')
    actions.store('dir', actions.random_str())
    actions.store('subdir', '{}.{}'.format(data.dir, actions.random_str()))
    project.create_test_directory(data.project, data.dir)
    project.create_test_directory(data.project, data.subdir)


def test(data):
    response = test_.rename_test_directory(data.project, data.subdir, data.dir)
    assert response.json()['errors'] == ['Path {} already exists'.format(data.dir)]
