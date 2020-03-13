from projects.golem_api.pages import users


def test(data):
    response = users.delete_user('does_not_exist')
    assert response.status_code == 200
    assert response.json() == {'errors': ['Username does_not_exist does not exist']}
