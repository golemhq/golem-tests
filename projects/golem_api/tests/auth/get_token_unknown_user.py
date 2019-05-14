
pages = ['auth']


def test(data):
    response = auth.get_token_request('unknown_user_01', 'does not matter')
    assert response.status_code == 401
