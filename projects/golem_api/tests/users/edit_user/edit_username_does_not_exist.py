from projects.golem_api.pages import users


def test(data):
    response = users.edit_user('username_not_exist')
    assert response.status_code == 200
    assert response.json() == ['Username username_not_exist does not exist']
