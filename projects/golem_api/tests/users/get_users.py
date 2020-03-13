from projects.golem_api.pages import users


def test(data):
    response = users.get_users()
    assert response.status_code == 200
