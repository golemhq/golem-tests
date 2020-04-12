from projects.golem_api.pages import project
from projects.golem_api.pages import suite
from projects.golem_api.pages import report


def setup(data):
    data.project = project.create_random_project()


def test(data):
    # project without executions
    response = project.get_project_health(data.project)
    assert response.status_code == 200
    assert response.json() == {}

    # project with one execution without tests
    suite_name = project.create_random_suite(data.project)
    response = suite.run_suite(data.project, suite_name)
    timestamp = response.json()
    report.wait_for_execution_to_finish(data.project, suite_name, timestamp)

    response = project.get_project_health(data.project)

    assert response.json()[suite_name]['total'] == 0
    assert response.json()[suite_name]['execution'] == timestamp
    assert response.json()[suite_name]['totals_by_result'] == {}

    # project with two executions, last one has one test
    # project-health should return the last one
    test_name = project.create_random_test(data.project)
    suite.save_suite(data.project, suite_name, tests=[test_name])
    response = suite.run_suite(data.project, suite_name)
    timestamp = response.json()
    report.wait_for_execution_to_finish(data.project, suite_name, timestamp)

    response = project.get_project_health(data.project)

    assert response.json()[suite_name]['total'] == 1
    assert response.json()[suite_name]['execution'] == timestamp
    assert response.json()[suite_name]['totals_by_result'] == {'success': 1}
