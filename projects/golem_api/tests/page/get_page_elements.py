
pages = ['project', 'page']


def setup(data):
    store('project', 'general_project')
    store('page', random('dddddd'))
    project.create_project_if(data.project)
    project.create_project_page(data.project, data.page)


def test(data):
    response = page.get_page_elements(data.project, data.page)
    assert response.status_code == 200
    assert response.json()['error'] == ''
    assert response.json()['contents'] == []
