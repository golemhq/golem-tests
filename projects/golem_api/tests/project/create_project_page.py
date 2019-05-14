
pages = ['project']


def setup(data):
    store('project', 'general_project')
    project.create_project_if(data.project)


def test(data):
    store('page', random('dddddd'))
    response = project.create_project_page(data.project, data.page)
    assert response.status_code == 200
    json_ = response.json()
    assert json_['errors'] == []
    expected_element = {
        'full_path': data.page,
        'is_directory': False,
        'name': data.page,
        'type': 'page'
    }
    assert json_['element'] == expected_element
