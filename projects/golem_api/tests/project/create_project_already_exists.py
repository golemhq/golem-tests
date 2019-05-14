
pages = ['project']


def test(data):
    store('project', random('dddddd'))
    project.create_project(data.project)
    response = project.create_project(data.project)
    assert response.status_code == 200
    assert 'A project with that name already exists' in response.json()['errors']
