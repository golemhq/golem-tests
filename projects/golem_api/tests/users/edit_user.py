from golem import actions

from projects.golem_api.pages import users


def test_edit_user(data):
    username = actions.random_str()
    users.create_new_user(username, '123456', 'test@test.com')
    new_username = actions.random_str()
    new_email = 'test2@test.com'
    new_project_permissions = [{'project': "projectname", 'permission': "admin"}]
    response = users.edit_user(username, new_username, new_email, False, new_project_permissions)
    assert response.status_code == 200
    response = users.get_user(new_username)
    assert response.json()['username'] == new_username
    assert response.json()['email'] == new_email
    assert response.json()['is_superuser'] is False
    assert response.json()['projects'] == {'projectname': 'admin'}


def test_edit_user_convert_to_superuser(data):
    username = actions.random_str()
    users.create_new_user(username, '123456', 'test@test.com')
    response = users.get_user(username)
    assert response.json()['is_superuser'] is False

    users.edit_user(username, new_is_superuser=True)
    response = users.get_user(username)
    assert response.json()['is_superuser'] is True


def test_edit_user_invalid_email(data):
    username = actions.random_str()
    users.create_new_user(username, '123456', 'test@test.com')
    invalid_email = 'test@test'
    response = users.edit_user(username, new_email=invalid_email)
    assert response.status_code == 200
    assert response.json() == ['{} is not a valid email address'.format(invalid_email)]


def test_edit_user_existing_username(data):
    username1 = actions.random_str()
    username2 = actions.random_str()
    users.create_new_user(username1, '123456')
    users.create_new_user(username2, '123456')
    response = users.edit_user(username1, new_username=username2)
    assert response.status_code == 200
    assert response.json() == ['Username {} already exists'.format(username2)]


def test_edit_user_blank_username(data):
    username = actions.random_str()
    users.create_new_user(username, '123456', 'test@test.com')
    response = users.edit_user(username, new_username='')
    assert response.status_code == 200
    assert response.json() == ['Username cannot be blank']


def test_edit_user_doesnt_exist(data):
    username = actions.random_str()
    response = users.edit_user(username, new_username=actions.random_str())
    assert response.status_code == 200
    assert response.json() == ['Username {} does not exist'.format(username)]


def test(data):
    username = actions.random_str()
    users.create_new_user(username, '123456', 'test@test.com')
    new_username = actions.random_str()
    users.edit_user(username, new_username=new_username)
    response = users.get_user(new_username)
    assert response.json()['username'] == new_username
    assert response.json()['email'] == 'test@test.com'
    users.edit_user(new_username, new_email='test2@test.com')
    response = users.get_user(new_username)
    assert response.json()['username'] == new_username
    assert response.json()['email'] == 'test2@test.com'
