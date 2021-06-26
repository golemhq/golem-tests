from golem import actions

from projects.golem_api.pages import users
from projects.golem_api.pages import auth


def test_reset_user_password(data):
    username = actions.random_str()
    users.create_new_user(username, '123456', 'test@test.com')
    new_password = '234567'
    response = users.reset_password(username, new_password)
    assert response.status_code == 200
    assert response.json() == {'errors': []}
    response = auth.get_token_request(username, new_password)
    assert response.status_code == 200


def test_reset_user_password_blank(data):
    username = actions.random_str()
    users.create_new_user(username, '123456', 'test@test.com')
    response = users.reset_password(username, '')
    assert response.status_code == 200
    assert response.json() == {'errors': ['Password cannot be blank']}


def test_reset_password_user_doesnt_exist(data):
    username = actions.random_str()
    response = users.reset_password(username, '123456')
    assert response.status_code == 200
    assert response.json() == {'errors': ['Username {} does not exist'.format(username)]}
