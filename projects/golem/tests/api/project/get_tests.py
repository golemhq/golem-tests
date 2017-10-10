
description = 'Verify that the /project/get_tests/ API call returns response code 200'

pages = []

def setup(data):
    pass

def test(data):
    post('http://localhost:8000/project/get_tests/', params={'project': 'test'})
    assert_equals(data.last_response.status_code, 200)


def teardown(data):
    pass
