
description = 'Verify golem action delete_cookie'

def test(data):
    navigate('https://google.com')
    add_cookie({'name': 'foo', 'value': 'bar'})
    delete_cookie('foo')
    assert get_cookie('foo') == None
