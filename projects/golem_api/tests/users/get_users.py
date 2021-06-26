from projects.golem_api.pages import users
from projects.golem_api.pages import project
from projects.golem_api.pages import user_factory


def test_get_users(data):
    project.using_project('general')
    standard = user_factory.create_user_if('general__standard')
    response = users.get_users()
    assert response.status_code == 200
    filtered = [u for u in response.json() if u['username'] == standard['username']]
    assert len(filtered) == 1
    assert filtered[0]['projects'] == {'general': 'standard'}
    assert filtered[0]['is_superuser'] is False
