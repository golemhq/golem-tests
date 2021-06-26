import time

from golem import actions

from projects.golem_api.pages import project
from projects.golem_api.pages import report
from projects.golem_api.pages import test_


def setup(data):
    project.using_project('general')
    data.test = project.create_random_test(data.project)
    response = test_.run_test(data.project, data.test)
    actions.store('timestamp', response.json())


def test_get_test_status(data):
    for _ in range(10):
        response = report.get_test_status(data.project, data.test, data.timestamp)
        if response.json()['has_finished'] is True:
            break
        time.sleep(1)

    if response.json()['has_finished']:
        assert len(response.json()['sets']) == 1
    else:
        actions.fail('Test execution did not finish in time')
