from golem import actions


description = 'Verify golem action delete_cookie'

def test(data):
    actions.navigate('https://google.com')
    actions.add_cookie({'name': 'foo', 'value': 'bar'})
    actions.delete_cookie('foo')
    assert actions.get_cookie('foo') == None
