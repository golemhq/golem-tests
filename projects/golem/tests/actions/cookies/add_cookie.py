
description = 'Verify golem action add_cookie'

def test(data):
    navigate('https://google.com')
    add_cookie({'name': 'foo', 'value': 'bar'})
    verify_cookie_exists('foo')

