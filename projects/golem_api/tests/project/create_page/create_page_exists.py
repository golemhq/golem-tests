from projects.golem_api.pages import project


def setup(data):
    project.using_project('general')
    data.page = project.create_random_page(data.project)


def test(data):
    response = project.create_page(data.project, data.page)
    assert response.status_code == 200
    assert response.json()['errors'] == ['A page with that name already exists']
