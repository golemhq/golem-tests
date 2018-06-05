from golem import actions
from golem import execution


description = 'Verify step action'

def test(data):
    actions.step('this is a step')
    assert execution.steps == ['this is a step']
