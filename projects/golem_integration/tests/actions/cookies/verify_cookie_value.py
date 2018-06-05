from golem import actions


description = 'Verify golem action verify_cookie_value'

def test(data):
    actions.navigate(data.env.url)
    actions.add_cookie({'name': 'foo', 'value': 'bar'})
    actions.verify_cookie_value('foo', 'bar')
