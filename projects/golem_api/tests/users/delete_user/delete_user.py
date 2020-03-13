from golem import actions

from projects.golem_api.pages import users


def setup(data):
    actions.store('username', actions.random_str())
    users.create_new_user(data.username, '123456', 'test@test.com')


def test(data):
    response = users.delete_user(data.username)
    assert response.status_code == 200
    assert response.json() == {'errors': []}
    response = users.get_user(data.username)
    assert response.json() is None
