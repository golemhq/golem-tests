from golem import actions

from projects.golem_integration.pages import golem_steps


description = 'Verify step action'

def test(data):
    actions.step('this is a step')
    golem_steps.assert_last_step_message('this is a step')

