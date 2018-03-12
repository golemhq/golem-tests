
description = 'Verify golem action get_cookie'

def test(data):
    navigate('https://google.com')
    add_cookie({'name': 'foo', 'value': 'bar'})
    cookie = get_cookie('foo')
    assert cookie['value'] == 'bar'
