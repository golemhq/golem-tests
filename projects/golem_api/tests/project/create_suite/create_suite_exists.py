from projects.golem_api.pages import project


def setup(data):
    project.using_project('general')
    data.suite = project.create_random_suite(data.project)


def test(data):
    response = project.create_suite(data.project, data.suite)
    assert response.status_code == 200
    assert response.json()['errors'] == ['A suite with that name already exists']
