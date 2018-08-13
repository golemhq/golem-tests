from golem import actions
from golem import execution


description = 'Verify open_browser action'

def test(data):
    actions.open_browser()
    assert 'main' in execution.browsers.keys()
    actions.open_browser('other_browser')
    assert 'other_browser' in execution.browsers.keys()