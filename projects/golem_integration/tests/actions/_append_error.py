from golem import actions
from golem import execution


description = 'Verify _append_error adds an error to the last step'

def test(data):
    # append error when there are no steps
    try:
        actions._append_error('error message', description='error description')
    except Exception as e:
        assert 'there is no last step to append error' in e.args[0]
    # add a step and append an error to it
    actions._add_step('step message')
    actions._append_error('error message', description='error description')
    expected = {'message': 'error message', 'description': 'error description'}
    assert execution.steps[-1]['error'] == expected
    # append error when last step already contains an error
    try:
        actions._append_error('error message', description='error description')
    except Exception as e:
        assert 'last step already contains an error' in e.args[0]