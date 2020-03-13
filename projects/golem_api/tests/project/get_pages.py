from projects.golem_api.pages import project


def setup(data):
    data.project = project.create_random_project()


def test(data):
    response = project.get_pages(data.project)
    assert response.status_code == 200
    assert response.json() == []
