
pages = ['project']


def setup(data):
    store('project', 'general_project')
    project.create_project_if(data.project)


def test(data):
    response = project.get_project_tags(data.project)
    assert response.status_code == 200
