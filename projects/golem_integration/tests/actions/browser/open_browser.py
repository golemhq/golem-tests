from golem import actions
from golem import execution

from projects.golem_integration.pages import golem_steps


description = 'Verify browser action'

def test(data):
    actions.open_browser()
    golem_steps.assert_last_step_message('Open browser')
    assert 'main' in execution.browsers.keys()
    actions.open_browser('other_browser')
    assert 'other_browser' in execution.browsers.keys()