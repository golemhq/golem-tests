
pages = ['auth']


def test(data):
    response = auth.get_token_request(data.env.users.admin.username, 'incorrect_password')
    assert response.status_code == 401
