from golem import actions
from golem import execution

description = 'Verify set_browser_capability action'

def test(data):
    actions.set_browser_capability('my_capability', 'my_value')
    assert 'my_capability' in execution.browser_definition['capabilities']
    assert execution.browser_definition['capabilities']['my_capability'] == 'my_value'
