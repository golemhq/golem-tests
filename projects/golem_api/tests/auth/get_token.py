from projects.golem_api.pages import auth


def test_get_token(data):
    response = auth.get_token_request(data.env.users.admin.username, data.env.users.admin.password)
    assert response.status_code == 200
    assert type(response.json()) is str


def test_get_token_with_incorrect_password(data):
    response = auth.get_token_request(data.env.users.admin.username, 'incorrect_password')
    assert response.status_code == 401


def test_get_token_with_unknown_user(data):
    response = auth.get_token_request('unknown_user_01', 'does not matter')
    assert response.status_code == 401
