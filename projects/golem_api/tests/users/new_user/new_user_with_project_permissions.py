from golem import actions

from projects.golem_api.pages import users


def test(data):
    username = actions.random_str()
    email = ''
    password = '123456'
    is_superuser = True
    project_permissions = [{'project': "projectname", 'permission': "admin"}]
    response = users.create_new_user(username, password, email, is_superuser, project_permissions)
    assert response.status_code == 200
    response = users.get_user(username)
    assert response.status_code == 200
    assert response.json()['username'] == username
    assert response.json()['email'] is None
    assert response.json()['is_superuser']
    assert response.json()['projects'] == {'projectname': 'admin'}
