from golem import actions


description = 'Verify golem action get_cookies'


def test_get_cookies(data):
    actions.navigate('https://google.com')
    actions.add_cookie({'name': 'foo', 'value': 'bar'})
    cookies = actions.get_cookies()
    assert [x for x in cookies if x['value'] == 'bar']
