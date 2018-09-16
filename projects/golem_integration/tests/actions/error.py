from golem import actions

from projects.golem_integration.pages import golem_steps


description = 'Verify error action'

def test(data):
    actions.error('foo', 'bar')
    golem_steps.assert_last_step_message('ERROR')
    golem_steps.assert_last_error('foo', 'bar')
