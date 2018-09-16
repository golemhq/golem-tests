from golem import actions
from golem import execution


description = 'Verify function _add_error adds an error to context.errors'

def test(data):
    actions._add_error('error message', description='error description')
    expected = [{'message': 'error message', 'description': 'error description'}]
    assert execution.errors == expected
    actions._add_error('error message 2')
    expected = {'message': 'error message 2', 'description': ''}
    assert expected in execution.errors
    execution.errors = []