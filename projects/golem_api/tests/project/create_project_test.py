
pages = ['project']


def setup(data):
    store('project', 'general_project')
    project.create_project_if(data.project)


def test(data):
    store('test', random('dddddd'))
    response = project.create_project_test(data.project, data.test)
    assert response.status_code == 200
    json_ = response.json()
    assert json_['errors'] == []
    expected_element = {
        'full_path': data.test,
        'is_directory': False,
        'name': data.test,
        'type': 'test'
    }
    assert json_['element'] == expected_element
