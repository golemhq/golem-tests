from golem import actions

from projects.golem_api.pages import project
from projects.golem_api.pages import page


def setup(data):
    project.using_project('general')
    data.page = project.create_random_page(data.project)


def test_save_page(data):
    elements = [{'name': 'nm', 'selector': 'id', 'value': 'x', 'display_name': 'nm'}]
    response = page.save_page(data.project, data.page, elements=elements, functions=[],
                              import_lines=[])
    assert response.status_code == 200
    assert response.json() == 'page-saved'
    response = page.get_page_components(data.project, data.page)
    expected_elements = [
        {
            'display_name': 'nm',
            'full_name': '{}.nm'.format(data.page),
            'name': 'nm',
            'partial_name': '{}.nm'.format(data.page),
            'selector': 'id',
            'value': 'x'
        }
    ]
    assert response.json()['components']['elements'] == expected_elements


def test_save_page_does_not_exist(data):
    # if page does not exist it is created
    page_name = actions.random_str()
    response = page.save_page(data.project, page_name, elements=[], functions=[],
                              import_lines=[])
    assert response.status_code == 200
    assert response.json() == 'page-saved'
