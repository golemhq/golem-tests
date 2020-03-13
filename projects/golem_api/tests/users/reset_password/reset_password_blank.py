from golem import actions

from projects.golem_api.pages import users


def setup(data):
    actions.store('username', actions.random_str())
    users.create_new_user(data.username, '123456', 'test@test.com')


def test(data):
    response = users.reset_password(data.username, '')
    assert response.status_code == 200
    assert response.json() == {'errors': ['Password cannot be blank']}
