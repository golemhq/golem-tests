from golem import actions

from projects.golem_api.pages import users


def test(data):
    password = actions.random_str()
    response = users.create_new_user('', password)
    assert response.status_code == 200
    assert response.json() == ['Username cannot be blank']
