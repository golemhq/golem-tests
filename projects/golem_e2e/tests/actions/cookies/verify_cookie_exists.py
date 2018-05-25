
description = 'Verify golem action verify_cookie_exists'

def test(data):
    navigate('https://google.com')
    add_cookie({'name': 'foo', 'value': 'bar'})
    verify_cookie_exists('foo')

