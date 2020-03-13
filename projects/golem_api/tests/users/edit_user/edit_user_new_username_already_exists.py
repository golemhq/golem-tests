from golem import actions

from projects.golem_api.pages import users


def setup(data):
    actions.store('username1', actions.random_str())
    actions.store('username2', actions.random_str())
    users.create_new_user(data.username1, '123456')
    users.create_new_user(data.username2, '123456')


def test(data):
    response = users.edit_user(data.username1, new_username=data.username2)
    assert response.status_code == 200
    assert response.json() == ['Username {} already exists'.format(data.username2)]
