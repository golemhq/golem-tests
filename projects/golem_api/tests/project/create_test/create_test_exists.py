from projects.golem_api.pages import project


def setup(data):
    project.using_project('general')
    data.test_one = project.create_random_test(data.project)


def test(data):
    response = project.create_test(data.project, data.test_one)
    assert response.status_code == 200
    assert response.json()['errors'] == ['A test with that name already exists']
