from golem import actions


description = 'Verify golem action verify_cookie_present'

def test(data):
    actions.navigate(data.env.url)
    actions.add_cookie({'name': 'foo', 'value': 'bar'})
    actions.verify_cookie_exists('foo')

