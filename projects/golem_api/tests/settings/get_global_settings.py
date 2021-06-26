from projects.golem_api.pages import settings


def test_get_global_settings(data):
    response = settings.get_global_settings()
    assert response.status_code == 200
    assert response.json()['default_browser'] == 'chrome'
