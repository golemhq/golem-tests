from golem import actions


description = 'Verify golem action delete_all_cookies'

def test(data):
    actions.navigate('https://google.com')
    actions.add_cookie({'name': 'foo', 'value': 'bar'})
    actions.add_cookie({'name': 'baz', 'value': 'qux'})
    actions.delete_all_cookies()
    assert actions.get_cookie('foo') == None
    assert actions.get_cookie('baz') == None
