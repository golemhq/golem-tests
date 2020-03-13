from golem import actions

from projects.golem_api.pages import users


def setup(data):
    actions.store('username', actions.random_str())
    users.create_new_user(data.username, '123456', 'test@test.com')


def test(data):
    new_username = actions.random_str()
    users.edit_user(data.username, new_username=new_username)
    response = users.get_user(new_username)
    assert response.json()['username'] == new_username
    assert response.json()['email'] == 'test@test.com'
    users.edit_user(new_username, new_email='test2@test.com')
    response = users.get_user(new_username)
    assert response.json()['username'] == new_username
    assert response.json()['email'] == 'test2@test.com'
