from golem import execution
from golem import actions


description = 'Verify set_search_timeout action'

def test(data):
    current_search_timeout = execution.settings['search_timeout']
    actions.set_search_timeout(999)
    assert execution.settings['search_timeout'] == 999
    actions.set_search_timeout(9.99)
    assert execution.settings['search_timeout'] == 9.99
    try:
        actions.set_search_timeout('999')
    except ValueError:
        pass
    actions.set_search_timeout(current_search_timeout)
