
pages = ['project']


def setup(data):
    store('project', 'general_project')
    project.create_project_if(data.project)


def test(data):
    response = project.get_supported_browsers(data.project)
    assert response.status_code == 200
    assert len(response.json()) == 14
