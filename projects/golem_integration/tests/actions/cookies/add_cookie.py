from golem import actions

description = 'Verify golem action add_cookie'


def test_add_cookie(data):
    actions.navigate('https://google.com')
    cookie = {'name': 'foo', 'value': 'bar'}
    actions.add_cookie(cookie)
    actions.verify_cookie_present('foo')

