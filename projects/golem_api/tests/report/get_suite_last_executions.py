
pages = ['project', 'suite', 'report']


def setup(data):
    store('project', 'general_project')
    project.create_project_if(data.project)
    store('suite', random('ddddd'))
    project.create_project_suite(data.project, data.suite)
    store('test', random('ddddd'))
    project.create_project_test(data.project, data.test)
    suite.save_suite(data.project, data.suite, tests=[data.test])
    response = suite.run_suite(data.project, data.suite)
    store('timestamp', response.json())


def test(data):
    response = report.get_suite_last_executions([data.project], data.suite, limit=3)
    assert response.status_code == 200
