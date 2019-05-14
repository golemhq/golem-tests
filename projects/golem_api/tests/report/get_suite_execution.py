
pages = ['project', 'suite', 'report']


def setup(data):
    store('project', 'general_project')
    project.create_project_if(data.project)
    store('suite', random('ddddd'))
    project.create_project_suite(data.project, data.suite)
    response = suite.run_suite(data.project, data.suite)
    store('timestamp', response.json())


def test(data):
    response = report.get_suite_execution(data.project, data.suite, data.timestamp)
    assert response.status_code == 200
    assert response.json()['tests'] == []
