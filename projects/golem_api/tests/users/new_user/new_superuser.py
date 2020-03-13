from golem import actions

from projects.golem_api.pages import users


def test(data):
    username = actions.random_str()
    email = ''
    password = actions.random_str()
    is_superuser = False
    project_permissions = []
    response = users.create_new_user(username, password, email, is_superuser, project_permissions)
    assert response.status_code == 200
    response = users.get_user(username)
    assert response.status_code == 200
    assert response.json()['username'] == username
    assert response.json()['email'] is None
    assert not response.json()['is_superuser']
    assert response.json()['projects'] == {}
