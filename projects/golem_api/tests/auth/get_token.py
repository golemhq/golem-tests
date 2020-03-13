from projects.golem_api.pages import auth


def test(data):
    response = auth.get_token_request(data.env.users.admin.username, data.env.users.admin.password)
    assert response.status_code == 200
    assert type(response.json()) is str
