from golem import actions

from projects.golem_api.pages import users
from projects.golem_api.pages import auth


def setup(data):
    actions.store('username', actions.random_str())
    users.create_new_user(data.username, '123456', 'test@test.com')


def test(data):
    new_password = '234567'
    response = users.reset_password(data.username, new_password)
    assert response.status_code == 200
    assert response.json() == {'errors': []}
    response = auth.get_token_request(data.username, new_password)
    assert response.status_code == 200
