from golem import actions

from projects.golem_api.pages import project


def setup(data):
    project.using_project('general')


def test(data):
    # invalid chars
    response = project.create_test(data.project, 'name-{}'.format(actions.random_str()))
    assert response.status_code == 200
    assert response.json()['errors'] == ['Only letters, numbers and underscores are allowed']
    # empty directory
    response = project.create_test(data.project, '.test_name')
    assert response.json()['errors'] == ['Directory name cannot be empty']
    # max length
    response = project.create_test(data.project, 'a'*151)
    assert response.json()['errors'] == ['Maximum name length is 150 characters']
    # empty name
    response = project.create_test(data.project, '')
    assert response.json()['errors'] == ['File name cannot be empty']
