from golem import actions


description = 'Verify golem action get_cookie'

def test(data):
    actions.navigate('https://google.com')
    actions.add_cookie({'name': 'foo', 'value': 'bar'})
    cookie = actions.get_cookie('foo')
    assert cookie['value'] == 'bar'
