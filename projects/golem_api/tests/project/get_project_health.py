
pages = ['project']


def setup(data):
    store('project', random('dddddd'))
    project.create_project(data.project)


def test(data):
    response = project.get_project_health(data.project)
    assert response.status_code == 200
    assert response.json() == {}
