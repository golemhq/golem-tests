
pages = ['project', 'test_']


def setup(data):
    store('project', 'general_project')
    store('test', random('dddddd'))
    project.create_project_if(data.project)
    project.create_project_test(data.project, data.test)


def test(data):
    steps = {'setup': [], 'test': [], 'teardown': []}
    response = test_.save_test(data.project, data.test, description='',
                               pages=[], test_data=[], steps=steps, tags=[])
    assert response.status_code == 200
    assert response.json() == 'test-saved'
