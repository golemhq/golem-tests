
description = 'Verify a post request to /login/ returns status code 200'


def test(data):
    http_post(data.env.url + 'login/', {}, {'username': '', 'password': '', 'next': ''})
    assert data.last_response.status_code == 200
