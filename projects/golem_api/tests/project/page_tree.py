from projects.golem_api.pages import project


def setup(data):
    data.project = project.create_random_project()


def test_project_page_tree(data):
    response = project.get_page_tree(data.project)
    assert response.status_code == 200
    assert response.json() == {
        'dot_path': '', 'name': 'pages', 'sub_elements': [], 'type': 'directory'
    }
