from projects.golem_api.pages import project
from projects.golem_api.pages import test_


def setup(data):
    project.using_project('general')
    data.test = project.create_random_test(data.project)


def test(data):
    steps = {
        'setup': [],
        'tests': {
            'test': []
        },
        'teardown': []
    }
    response = test_.save_test(data.project, data.test, description='',
                               pages=[], test_data=[], steps=steps, tags=[], skip=False)
    assert response.status_code == 200
    assert response.json() == 'test-saved'
