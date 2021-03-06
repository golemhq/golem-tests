from golem import actions

from projects.golem_integration.pages import golem_steps


description = 'Verify golem action add_cookie'

def test(data):
    actions.navigate('https://google.com')
    cookie = {'name': 'foo', 'value': 'bar'}
    actions.add_cookie(cookie)
    actions.verify_cookie_exists('foo')

