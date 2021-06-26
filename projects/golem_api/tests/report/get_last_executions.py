from projects.golem_api.pages import project
from projects.golem_api.pages import suite
from projects.golem_api.pages import report


def setup(data):
    project.using_project('general')
    data.suite = project.create_random_suite(data.project)
    response = suite.run_suite(data.project, data.suite)
    data.timestamp = response.json()
    report.wait_for_execution_to_finish(data.project, data.suite, data.timestamp)


def test_get_last_executions(data):
    response = report.get_last_executions()
    assert response.status_code == 200
    proj = response.json()['projects'][data.project]
    execution = proj[data.suite]
    assert execution == [data.timestamp]


def test_get_project_last_executions(data):
    response = report.get_project_last_executions(data.project)
    assert response.status_code == 200
    proj = response.json()['projects'][data.project]
    execution = proj[data.suite]
    assert execution == [data.timestamp]


def test_get_execution_last_executions(data):
    response = report.get_execution_last_executions(data.project, data.suite)
    assert response.status_code == 200
    proj = response.json()['projects'][data.project]
    execution = proj[data.suite]
    assert execution == [data.timestamp]
