
pages = ['project']


def test(data):
    store('project', random('dddddd'))
    response = project.create_project(data.project)
    assert response.status_code == 200
    assert response.json()['errors'] == []
    assert response.json()['project_name'] == data.project
    response = project.get_project_exists(data.project)
    assert response.json() is True
