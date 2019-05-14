
pages = ['project', 'page']


def setup(data):
    store('project', 'general_project')
    store('page', random('dddddd'))
    project.create_project_if(data.project)
    project.create_project_page(data.project, data.page)


def test(data):
    response = page.save_page_code(data.project, data.page, content='')
    assert response.status_code == 200
    assert response.json()['error'] is None
