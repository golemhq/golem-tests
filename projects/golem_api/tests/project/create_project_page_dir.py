
pages = ['project']


def setup(data):
    store('project', 'general_project')
    project.create_project_if(data.project)


def test(data):
    store('dir_name', random('dddddd'))
    response = project.create_project_page(data.project, data.dir_name, is_dir=True)
    assert response.status_code == 200
    json_ = response.json()
    assert json_['errors'] == []
    expected_element = {
        'full_path': data.dir_name,
        'is_directory': True,
        'name': data.dir_name,
        'type': 'page'
    }
    assert json_['element'] == expected_element
