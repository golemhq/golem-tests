from golem import actions
from golem import execution

from projects.golem_integration.utils import expected_exception


description = 'Verify _append_error adds an error to the last step'

def test(data):
    # append error when there are no steps
    with expected_exception(Exception, 'there is no last step to append error'):
        actions._append_error('error message', description='error description')
    # add a step and append an error to it
    actions._add_step('step message')
    actions._append_error('error message', description='error description')
    expected = {'message': 'error message', 'description': 'error description'}
    assert execution.steps[-1]['error'] == expected
    # append error when last step already contains an error
    with expected_exception(Exception, 'last step already contains an error'):
        actions._append_error('error message', description='error description')
