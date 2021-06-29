from projects.golem_api.pages import project
from projects.golem_api.pages import test_


def setup(data):
    project.using_project('general')


def test_save_test_code(data):
    test_name = project.create_test(data.project)
    code = 'def test_one(data):\n    assert True'
    test_.save_test_code(data.project, test_name, test_data='', content=code)

    response = test_.get_test_components(data.project, test_name)
    expected = {
        'code': 'def test_one(data):\n    assert True',
        'description': '',
        'pages': [],
        'setup_steps': None,
        'skip': False,
        'tags': [],
        'teardown_steps': None,
        'test_function_list': ['test_one'],
        'test_functions': {
            'test_one': [{'code': 'assert True', 'type': 'code-block'}]
        }
    }
    assert response.json()['components'] == expected
