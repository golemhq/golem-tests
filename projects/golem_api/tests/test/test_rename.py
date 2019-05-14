
pages = ['project', 'test_']


def setup(data):
    store('project', 'general_project')
    store('test', random('dddddd'))
    project.create_project_if(data.project)
    project.create_project_test(data.project, data.test)


def test(data):
    store('new_test_name', random('dddddd'))
    response = test_.rename_test(data.project, data.test, data.new_test_name)
    assert response.status_code == 200
    assert response.json()['error'] == ''
