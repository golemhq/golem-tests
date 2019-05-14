
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
    report.wait_for_execution_to_finish(data.project, data.suite, data.timestamp)
    response = report.get_suite_execution(data.project, data.suite, data.timestamp)
    test_set = response.json()['tests'][0]['test_set']
    response = report.get_test_set(data.project, data.suite, data.timestamp, data.test, test_set)
    assert response.status_code == 200
    assert response.json()['result'] == 'success'
