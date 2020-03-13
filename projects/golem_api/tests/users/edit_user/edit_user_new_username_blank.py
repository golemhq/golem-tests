from golem import actions

from projects.golem_api.pages import users


def setup(data):
    actions.store('username', actions.random_str())
    users.create_new_user(data.username, '123456', 'test@test.com')


def test(data):
    response = users.edit_user(data.username, new_username='')
    assert response.status_code == 200
    assert response.json() == ['Username cannot be blank']
