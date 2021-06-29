from projects.golem_api.pages import project
from projects.golem_api.pages import test_


def setup(data):
    project.using_project('general')


def test_save_test(data):
    test_name = project.create_test(data.project)
    steps = {
        'setup': [],
        'tests': {
            'test_one': [
                {'type': 'function-call', 'action': 'step', 'parameters': ["'msg'"]}
            ]
        },
        'teardown': []
    }
    response = test_.save_test(data.project, test_name, description='', pages=[],
                               test_data=[], steps=steps, tags=[], skip=False)
    assert response.status_code == 200
    assert response.json() == 'test-saved'

    response = test_.get_test_components(data.project, test_name)
    expected = [{
        'code': "step('msg')",
        'function_name': 'step',
        'parameters': ["'msg'"],
        'type': 'function-call'
    }]
    assert response.json()['components']['test_functions']['test_one'] == expected
