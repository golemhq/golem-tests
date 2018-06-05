from golem import execution
from golem import actions


description = 'Verify get_search_timeout action'

def test(data):
    current_search_timeout = execution.settings['search_timeout']
    actions.set_search_timeout(999)
    assert actions.get_search_timeout() == 999
    actions.set_search_timeout(current_search_timeout)
