from golem import actions

from projects.golem_api.pages import users


def test(data):
    username = actions.random_str()
    users.create_new_user(username, '123456')
    response = users.create_new_user(username, '123456')
    assert response.status_code == 200
    assert response.json() == ['Username {} already exists'.format(username)]
