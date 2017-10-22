
description = 'Verify that a get request to /login/ returns status code 200'

pages = []

def setup(data):
    pass

def test(data):
    http_get(data.env.url + '/login/')
    assert_equals(data.last_response.status_code, 200)


def teardown(data):
    pass
