
pages = ['project']


def setup(data):
    store('project', 'general_project')
    project.create_project_if(data.project)


def test(data):
    store('page', random('dddddd'))
    response = project.get_project_page_exists(data.project, data.page)
    assert response.json() is False
    project.create_project_page(data.project, data.page)
    response = project.get_project_page_exists(data.project, data.page)
    assert response.json() is True
