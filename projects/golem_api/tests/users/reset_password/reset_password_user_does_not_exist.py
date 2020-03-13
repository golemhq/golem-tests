from projects.golem_api.pages import users


def test(data):
    response = users.reset_password('not_exist', '123456')
    assert response.status_code == 200
    assert response.json() == {'errors': ['Username not_exist does not exist']}
