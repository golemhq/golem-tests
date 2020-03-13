from golem import actions

from projects.golem_api.pages import users


def setup(data):
    actions.store('username', actions.random_str())
    users.create_new_user(data.username, '123456', 'test@test.com')


def test(data):
    response = users.get_user(data.username)
    assert response.json()['is_superuser'] is False
    users.edit_user(data.username, new_is_superuser=True)
    response = users.get_user(data.username)
    assert response.json()['is_superuser'] is True
