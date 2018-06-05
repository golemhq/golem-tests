from golem import actions
from golem import execution


description = 'Verify store action'

def test(data):
    actions.store('a key', 'a value')
    assert execution.data['a key'] == 'a value'
