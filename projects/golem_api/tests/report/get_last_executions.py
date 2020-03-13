from projects.golem_api.pages import report


def test(data):
    response = report.get_last_executions()
    assert response.status_code == 200
