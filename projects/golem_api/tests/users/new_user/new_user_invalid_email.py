from golem import actions

from projects.golem_api.pages import users


def test(data):
    username = actions.random_str()
    email = 'invalid@email'
    response = users.create_new_user(username, '123456', email)
    assert response.status_code == 200
    assert response.json() == ['{} is not a valid email address'.format(email)]
