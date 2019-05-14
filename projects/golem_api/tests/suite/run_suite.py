
pages = ['project', 'suite']


def setup(data):
    store('project', 'general_project')
    store('suite', random('dddddd'))
    project.create_project_if(data.project)
    project.create_project_suite(data.project, data.suite)


def test(data):
    response = suite.run_suite(data.project, data.suite)
    assert response.status_code == 200
    assert type(response.json()) == str
