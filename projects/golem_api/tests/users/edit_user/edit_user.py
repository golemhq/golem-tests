from golem import actions

from projects.golem_api.pages import users


def setup(data):
    actions.store('username', actions.random_str())
    users.create_new_user(data.username, '123456', 'test@test.com')


def test(data):
    new_username = actions.random_str()
    new_email = 'test2@test.com'
    new_project_permissions = [{'project': "projectname", 'permission': "admin"}]
    response = users.edit_user(data.username, new_username, new_email, False, new_project_permissions)
    assert response.status_code == 200
    response = users.get_user(new_username)
    assert response.json()['username'] == new_username
    assert response.json()['email'] == new_email
    assert response.json()['is_superuser'] is False
    assert response.json()['projects'] == {'projectname': 'admin'}
