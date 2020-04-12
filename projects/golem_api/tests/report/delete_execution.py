from golem import actions

from projects.golem_api.pages import project
from projects.golem_api.pages import suite
from projects.golem_api.pages import report


def setup(data):
    project.using_project('general')


def test(data):
    # execution does not exist
    suite_name = project.create_random_suite(data.project)
    timestamp = actions.random_str()
    response = report.delete_execution(data.project, suite_name, timestamp)
    assert response.status_code == 200
    assert response.json() == ['Execution for {} {} {} does not exist'.format(data.project, suite_name, timestamp)]

    # delete execution
    response = suite.run_suite(data.project, suite_name)
    timestamp = response.json()
    report.wait_for_execution_to_finish(data.project, suite_name, timestamp)

    response = report.delete_execution(data.project, suite_name, timestamp)

    assert response.status_code == 200
    assert response.json() == []
