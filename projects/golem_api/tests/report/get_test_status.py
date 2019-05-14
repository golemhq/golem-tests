
pages = ['project', 'test_', 'report']


def setup(data):
    store('project', 'general_project')
    project.create_project_if(data.project)
    store('test', random('ddddd'))
    project.create_project_test(data.project, data.test)
    response = test_.run_test(data.project, data.test)
    store('timestamp', response.json())


def test(data):
    response = report.get_test_status(data.project, data.test, data.timestamp)
    assert response.status_code == 200
