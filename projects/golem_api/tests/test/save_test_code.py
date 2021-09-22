from projects.golem_api.pages import project
from projects.golem_api.pages import test_


def setup(data):
    project.using_project('general')


def test_save_test_code(data):
    test_name = project.create_random_test(data.project)
    code = 'def test_one(data):\n    assert True'
    response = test_.save_test_code(data.project, test_name, code)
    assert response.status_code == 200
    assert response.json()['testError'] is None
    assert response.json()['dataErrors'] == []
    response = test_.get_test_components(data.project, test_name)
    assert response.json()['components']['code'] == code


def test_save_test_code_with_an_error(data):
    test_name = project.create_random_test(data.project)
    code = 'def test_one(data):\n    print('
    response = test_.save_test_code(data.project, test_name, code)
    assert response.status_code == 200
    assert 'print(' in response.json()['testError']
    assert 'SyntaxError: unexpected EOF while parsing' in response.json()['testError']
    assert response.json()['dataErrors'] == []


def test_save_test_code_with_csv_data(data):
    test_name = project.create_random_test(data.project)
    test_data = {
        'csv': [{'a': 'b'}],
        'json': None,
        'internal': None
    }
    response = test_.save_test_code(data.project, test_name, '', test_data)
    assert response.status_code == 200
    assert response.json()['testError'] is None
    assert response.json()['dataErrors'] == []


def test_save_test_code_with_json_data_invalid_json(data):
    test_name = project.create_random_test(data.project)
    test_data = {
        'csv': None,
        'json': '[{"a": "b}]',
        'internal': None
    }
    response = test_.save_test_code(data.project, test_name, '', test_data)
    assert response.status_code == 200
    assert response.json()['testError'] is None
    assert len(response.json()['dataErrors']) == 1
    error = 'json.decoder.JSONDecodeError: Unterminated string starting at: line 1 column 8'
    assert error in response.json()['dataErrors'][0]
