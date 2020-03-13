from projects.golem_api.pages import settings


def test(data):
    response = settings.get_global_settings()
    assert response.status_code == 200
