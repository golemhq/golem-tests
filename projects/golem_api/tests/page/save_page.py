
pages = ['project', 'page']


def setup(data):
    store('project', 'general_project')
    store('page', random('dddddd'))
    project.create_project_if(data.project)
    project.create_project_page(data.project, data.page)


def test(data):
    response = page.save_page(data.project, data.page, elements=[], functions=[],
                              import_lines=[])
    assert response.status_code == 200
    assert response.json() == 'page-saved'
