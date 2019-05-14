
pages = ['project', 'page']


def setup(data):
    store('project', 'general_project')
    store('page', random('dddddd'))
    project.create_project_if(data.project)
    project.create_project_page(data.project, data.page)


def test(data):
    store('new_page_name', random('dddddd'))
    response = page.duplicate_page(data.project, data.page, data.new_page_name)
    assert response.status_code == 200
    assert response.json() == []
    response = project.get_project_page_exists(data.project, data.new_page_name)
    assert response.json() is True
