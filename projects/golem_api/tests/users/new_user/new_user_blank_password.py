from golem import actions

from projects.golem_api.pages import users


def test(data):
    username = actions.random_str()
    response = users.create_new_user(username, '')
    assert response.status_code == 200
    assert response.json() == ['Password cannot be blank']
