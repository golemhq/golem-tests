from golem import actions

description = 'Verify golem action add_cookie'

def test(data):
    actions.navigate('https://google.com')
    actions.add_cookie({'name': 'foo', 'value': 'bar'})
    actions.verify_cookie_exists('foo')

