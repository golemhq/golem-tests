from projects.golem_api.pages import project


def setup(data):
    data.project = project.create_random_project()
    data.test = project.create_random_test(data.project)


def test_get_test_tree(data):
    response = project.get_test_tree(data.project)
    assert response.status_code == 200
    expected = {
        'dot_path': '',
        'name': 'tests',
        'sub_elements': [{
            'dot_path': data.test,
            'name': data.test,
            'sub_elements': [],
            'type': 'file'
        }],
        'type': 'directory'
    }
    assert response.json() == expected
