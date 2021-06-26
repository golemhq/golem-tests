from projects.golem_api.pages import project


def setup(data):
    data.project = project.create_random_project()


def test_suite_tree(data):
    response = project.get_suite_tree(data.project)
    assert response.status_code == 200
    assert response.json() == {
        'dot_path': '', 'name': 'suites', 'sub_elements': [], 'type': 'directory'
    }
