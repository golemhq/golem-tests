from golem import actions

from projects.golem_api.pages import users


def test_delete_user(data):
    username = actions.random_str()
    users.create_new_user(username, '123456', 'test@test.com')
    response = users.delete_user(username)
    assert response.status_code == 200
    assert response.json() == {'errors': []}
    response = users.get_user(username)
    assert response.json() is None


def test_delete_user_doesnt_exist(data):
    username = actions.random_str()
    response = users.delete_user(username)
    assert response.status_code == 200
    assert response.json() == {'errors': ['Username {} does not exist'.format(username)]}
