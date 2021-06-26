from golem import actions

from projects.golem_api.pages import users


def test_new_user(data):
    username = actions.random_str()
    email = ''
    password = actions.random_str()
    is_superuser = True
    project_permissions = []
    response = users.create_new_user(username, password, email, is_superuser, project_permissions)
    assert response.status_code == 200
    assert response.json() == []
    response = users.get_user(username)
    assert response.json()['username'] == username
    assert response.json()['email'] is None
    assert response.json()['is_superuser'] is True
    assert response.json()['projects'] == {}


def test_new_user_already_exists(data):
    username = actions.random_str()
    users.create_new_user(username, '123456')
    response = users.create_new_user(username, '123456')
    assert response.status_code == 200
    assert response.json() == ['Username {} already exists'.format(username)]


def test_new_user_blank_password(data):
    response = users.create_new_user(actions.random_str(), '')
    assert response.status_code == 200
    assert response.json() == ['Password cannot be blank']


def test_new_user_blank_username(data):
    response = users.create_new_user('', actions.random_str())
    assert response.status_code == 200
    assert response.json() == ['Username cannot be blank']


def test_new_user_invalid_email(data):
    email = 'invalid@email'
    response = users.create_new_user(actions.random_str(), '123456', email)
    assert response.status_code == 200
    assert response.json() == ['{} is not a valid email address'.format(email)]


def test_new_user_with_project_permissions(data):
    username = actions.random_str()
    password = '123456'
    is_superuser = False
    project_permissions = [{'project': "projectname", 'permission': "admin"}]
    response = users.create_new_user(username, password, '', is_superuser, project_permissions)
    assert response.status_code == 200
    assert response.json() == []
    response = users.get_user(username)
    assert response.json()['username'] == username
    assert response.json()['email'] is None
    assert response.json()['is_superuser'] is False
    assert response.json()['projects'] == {'projectname': 'admin'}


def test_new_superuser(data):
    username = actions.random_str()
    password = actions.random_str()
    is_superuser = True
    project_permissions = []
    response = users.create_new_user(username, password, '', is_superuser, project_permissions)
    assert response.status_code == 200
    response = users.get_user(username)
    assert response.json()['username'] == username
    assert response.json()['email'] is None
    assert response.json()['is_superuser'] is True
    assert response.json()['projects'] == {}
