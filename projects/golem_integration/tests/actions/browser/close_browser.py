from golem import actions
from golem import execution

from projects.golem_integration.pages import golem_steps


description = 'Verify close_browser action'

def test(data):
    actions.navigate(data.env.url)
    actions.close_browser()
    golem_steps.assert_last_step_message('Close browser')
    assert execution.browser is None
