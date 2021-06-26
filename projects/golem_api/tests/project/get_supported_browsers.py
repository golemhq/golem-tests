from projects.golem_api.pages import project


def setup(data):
    project.using_project('general')


def test_supported_browsers(data):
    response = project.get_supported_browsers(data.project)
    assert response.status_code == 200
    assert len(response.json()) == 14
    assert 'chrome' in response.json()
