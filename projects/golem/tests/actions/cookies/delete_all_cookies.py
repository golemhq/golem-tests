
description = 'Verify golem action delete_all_cookies'

def test(data):
    navigate('https://google.com')
    add_cookie({'name': 'foo', 'value': 'bar'})
    add_cookie({'name': 'baz', 'value': 'qux'})
    delete_all_cookies()
    assert get_cookie('foo') == None
    assert get_cookie('baz') == None
