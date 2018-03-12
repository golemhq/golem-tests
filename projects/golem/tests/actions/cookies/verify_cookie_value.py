
description = 'Verify golem action verify_cookie_value'

def test(data):
    navigate('https://google.com')
    add_cookie({'name': 'foo', 'value': 'bar'})
    verify_cookie_value('foo', 'bar')
