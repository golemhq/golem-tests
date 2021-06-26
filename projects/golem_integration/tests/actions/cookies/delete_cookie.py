from golem import actions

from projects.golem_integration.pages import golem_steps


description = 'Verify golem action delete_cookie'


def test_delete_cookie(data):
    actions.navigate('https://google.com')
    actions.add_cookie({'name': 'foo', 'value': 'bar'})
    actions.delete_cookie('foo')
    golem_steps.assert_last_step_message("Delete cookie 'foo'")
    assert actions.get_cookie('foo') is None

