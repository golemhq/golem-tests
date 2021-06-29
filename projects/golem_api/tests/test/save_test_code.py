from projects.golem_api.pages import project
from projects.golem_api.pages import test_


def setup(data):
    project.using_project('general')


def test_save_test_code(data):
    test_name = project.create_test(data.project)
    code = 'def test_one(data):\n    assert True'
    response = test_.save_test_code(data.project, test_name, test_data='', content=code)
    assert response.status_code == 200
    assert response.json()['error'] is None
    response = test_.get_test_components(data.project, test_name)
    assert response.json()['components']['code'] == code


def test_save_test_code_with_an_error(data):
    test_name = project.create_test(data.project)
    code = 'def test_one(data):\n    print('
    response = test_.save_test_code(data.project, test_name, test_data='', content=code)
    assert response.status_code == 200
    assert 'print(' in response.json()['error']
    assert 'SyntaxError: unexpected EOF while parsing' in response.json()['error']
