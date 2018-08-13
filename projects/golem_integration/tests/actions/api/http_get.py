from golem import actions

description = 'Verify http_get action'


def test(data):
    actions.http_get(data.env.url)
    assert data.last_response.status_code == 200
