from golem import execution
from golem import actions

from projects.golem_integration.utils import expected_exception


description = 'Verify set_search_timeout action'

def test(data):
    current_search_timeout = execution.settings['search_timeout']
    actions.set_search_timeout(999)
    assert execution.settings['search_timeout'] == 999
    actions.set_search_timeout(9.99)
    assert execution.settings['search_timeout'] == 9.99
    with expected_exception(ValueError):
        actions.set_search_timeout('999')
    actions.set_search_timeout(current_search_timeout)
