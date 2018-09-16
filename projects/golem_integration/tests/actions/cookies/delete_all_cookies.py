from golem import actions

from projects.golem_integration.pages import golem_steps


description = 'Verify golem action delete_all_cookies'

def test(data):
    actions.navigate('https://google.com')
    actions.add_cookie({'name': 'foo', 'value': 'bar'})
    actions.add_cookie({'name': 'baz', 'value': 'qux'})
    actions.delete_all_cookies()
    golem_steps.assert_last_step_message('Delete all cookies')
    assert actions.get_cookie('foo') is None
    assert actions.get_cookie('baz') is None
