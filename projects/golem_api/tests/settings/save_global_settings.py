from projects.golem_api.pages import settings


def test(data):
    response = settings.save_global_settings('{}')
    assert response.status_code == 200
    assert response.json() == 'settings-saved'
