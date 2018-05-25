
description = 'Verify a post request to /login/ returns status code 200'

pages = []

def setup(data):
    pass

def test(data):
    http_post(data.env.url + '/login/', {}, {'username': '', 'password': '', 'next': ''})
    assert_equals(data.last_response.status_code, 200)


def teardown(data):
    pass
