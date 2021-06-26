from projects.golem_api.pages import project


def setup(data):
    data.project = project.create_random_project()


def test_project_pages(data):
    response = project.get_pages(data.project)
    assert response.status_code == 200
    assert response.json() == []
    page_name = project.create_random_page(data.project)
    response = project.get_pages(data.project)
    assert response.json() == [page_name]
