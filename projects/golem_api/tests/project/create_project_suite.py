
pages = ['project']


def setup(data):
    store('project', 'general_project')
    project.create_project_if(data.project)


def test(data):
    store('suite', random('dddddd'))
    response = project.create_project_suite(data.project, data.suite)
    assert response.status_code == 200
    json_ = response.json()
    assert json_['errors'] == []
    expected_element = {
        'full_path': data.suite,
        'is_directory': False,
        'name': data.suite,
        'type': 'suite'
    }
    assert json_['element'] == expected_element
