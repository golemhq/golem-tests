from golem import actions

description = 'Verify golem action add_cookie'


def test(data):
    actions.navigate('https://google.com')
    cookie = {'name': 'foo', 'value': 'bar'}
    actions.add_cookie(cookie)
    actions.verify_cookie_present('foo')

