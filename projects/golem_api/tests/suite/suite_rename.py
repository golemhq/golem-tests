
pages = ['project', 'suite']


def setup(data):
    store('project', 'general_project')
    store('suite', random('dddddd'))
    project.create_project_if(data.project)
    project.create_project_suite(data.project, data.suite)


def test(data):
    store('new_suite_name', random('dddddd'))
    response = suite.rename_suite(data.project, data.suite, data.new_suite_name)
    assert response.status_code == 200
    assert response.json()['error'] == ''
