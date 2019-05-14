
pages = ['project', 'suite']


def setup(data):
    store('project', 'general_project')
    store('suite', random('dddddd'))
    project.create_project_if(data.project)
    project.create_project_suite(data.project, data.suite)


def test(data):
    response = suite.save_suite(data.project, data.suite, [], 1, [], [], [])
    assert response.status_code == 200
    assert response.json() == 'suite-saved'
