
description = 'Verify golem action get_cookies'

def test(data):
    navigate('https://google.com')
    add_cookie({'name': 'foo', 'value': 'bar'})
    cookies = get_cookies()
    assert [x for x in cookies if x['value'] == 'bar']
