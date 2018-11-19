
description = 'Verify a get request to /login/ returns status code 200'


def test(data):
    http_get(data.env.url + '/login/')
    assert data.last_response.status_code == 200
