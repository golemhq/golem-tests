from golem import actions

from projects.golem_integration.utils import expected_exception


description = 'Verify fail action'

def test(data):
    with expected_exception(AssertionError, 'I have failed you Anakin'):
        actions.fail('I have failed you Anakin')
