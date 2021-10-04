from projects.golem_api.pages import project
from projects.golem_api.pages import test_


def setup(data):
    project.using_project('general')


def test_save_test(data):
    test_name = project.create_random_test(data.project)
    steps = {
        'hooks': {},
        'tests': {
            'test_one': [
                {'type': 'function-call', 'action': 'step', 'parameters': ["'msg'"]}
            ]
        }
    }
    response = test_.save_test(data.project, test_name, description='', pages=[],
                               steps=steps, tags=[], skip=False)
    assert response.status_code == 200
    assert response.json()['errors'] == []

    response = test_.get_test_components(data.project, test_name)
    expected = [{
        'code': "step('msg')",
        'function_name': 'step',
        'parameters': ["'msg'"],
        'type': 'function-call'
    }]
    assert response.json()['components']['test_functions']['test_one'] == expected


def test_save_test_with_csv_data(data):
    test_name = project.create_random_test(data.project)
    test_data = {
        'csv': [{'a': 'b'}],
        'json': None,
        'internal': None
    }
    response = test_.save_test(data.project, test_name, test_data=test_data)
    assert response.status_code == 200
    assert response.json()['errors'] == []


def test_save_test_with_json_data(data):
    test_name = project.create_random_test(data.project)
    test_data = {
        'csv': None,
        'json': '[{"a": "b"}]',
        'internal': None
    }
    response = test_.save_test(data.project, test_name, test_data=test_data)
    assert response.status_code == 200
    assert response.json()['errors'] == []


def test_save_test_with_json_data_invalid_json(data):
    test_name = project.create_random_test(data.project)
    test_data = {
        'csv': None,
        'json': '[{"a": "b}]',
        'internal': None
    }
    response = test_.save_test(data.project, test_name, test_data=test_data)
    assert response.status_code == 200
    msg = 'json.decoder.JSONDecodeError: Unterminated string starting at: line 1 column 8'
    assert len(response.json()['errors']) == 1
    assert msg in response.json()['errors'][0]


def test_save_test_with_internal_data(data):
    test_name = project.create_random_test(data.project)
    test_data = {
        'csv': None,
        'json': None,
        'internal': 'data = [{"a": "b"}]'
    }
    response = test_.save_test(data.project, test_name, test_data=test_data)
    assert response.status_code == 200
    assert response.json()['errors'] == []


def test_save_test_with_internal_data_invalid(data):
    test_name = project.create_random_test(data.project)
    test_data = {
        'csv': None,
        'json': None,
        'internal': 'data = [{"a": "b}]'
    }
    response = test_.save_test(data.project, test_name, test_data=test_data)
    assert response.status_code == 200
    assert len(response.json()['errors']) == 1
    msg = 'SyntaxError: EOL while scanning string literal'
    assert msg in response.json()['errors'][0]
