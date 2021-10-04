from projects.golem_api.pages import project
from projects.golem_api.pages import test_


def setup(data):
    project.using_project('general')


def test_save_test_code(data):
    test_name = project.create_random_test(data.project)
    code = 'def test_one(data):\n    assert True'
    test_.save_test_code(data.project, test_name, code)

    response = test_.get_test_components(data.project, test_name)
    expected = {
        'description': '',
        'pages': [],
        'tags': [],
        'skip': False,
        'test_functions': {
            'test_one': [{'code': 'assert True', 'type': 'code-block'}]
        },
        'test_function_list': ['test_one'],
        'test_hooks': {},
        'test_hook_list': [],
        'code': 'def test_one(data):\n    assert True',
    }
    assert response.json()['components'] == expected
