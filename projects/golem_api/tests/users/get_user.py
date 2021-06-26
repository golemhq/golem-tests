from projects.golem_api.pages import users
from projects.golem_api.pages import project
from projects.golem_api.pages import user_factory


def test_get_user(data):
    project.using_project('general')
    standard = user_factory.create_user_if('general__standard')
    response = users.get_user(standard['username'])
    assert response.status_code == 200
    assert response.json()['projects'] == {'general': 'standard'}
    assert response.json()['username'] == standard['username']
    assert response.json()['email'] is None
    assert response.json()['is_superuser'] is False
